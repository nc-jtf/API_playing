import numpy as np
import pandas as pd
import random
import database_connection
import data_functions as load
import os
from generate_grn import *
from scripts.move_sheets_excel import pack_out


def guarantee_0_1_trader_query():
    '''Creates guarantees for the CVR's in the excel sheet without one. When set up, press "y" when asked to commit'''
    conn = database_connection.connection(database_connection.tfe_gms_db)
    cur = conn.cursor()
    cur.execute("SELECT MAX(sid) FROM dms.trader")
    n = 1
    row = cur.fetchone()
    if row is not None:
        max_sid = int(row[0])
        print('max sid number: ', max_sid)
    else:
        print("No rows returned from query")
    grn_type_0, grn_type_1 = np.array([], dtype=str), np.array([], dtype=str) #lister af grn oprettes

    for name_of_new_company, cvr_of_new_company in load.list_new_companies():
        cvr_of_new_company = load.make_CVR_EORI(cvr_of_new_company)
        new_sid = max_sid+n
        print("\nCompany: ", name_of_new_company, ". CVR: ", cvr_of_new_company)
        name_of_company = f"{name_of_new_company}"
        name_of_new_company = escape_single_quote(name_of_new_company)
        new_sid = get_sid(cvr_of_new_company, cur)
        # cur.execute(f'''
        # insert into trader    (sid, tin     , referenced,                 name, street_and_number, country_cl, post_code, city)
        # values		          ({new_sid}, '{cvr_of_new_company}',          '0', '{name_of_new_company}', '', 'DK', '', '');''')

        grn_type_0 = execute_guarantee(0, new_sid, cvr_of_new_company, name_of_new_company, cur, grn_type_0)
        grn_type_1 = execute_guarantee(1, new_sid, cvr_of_new_company, name_of_new_company, cur, grn_type_1)
        n = n + 1


    update_excel(grn_type_0, os.getcwd() + "\data\Firma garantier til fletning med breve Test.xlsx", 'Sheet1','New Type 0 GRN')
    update_excel(grn_type_1, os.getcwd() + "\data\Firma garantier til fletning med breve Test.xlsx", 'Sheet1','New Type 1 GRN')
    push = input("Is the querry satisfactory? press y to commit: ")
    if push == "y":
        conn.commit()
        print("Commit created")
    else:
        print("No commit created")

def execute_guarantee(guarantee_type, trader_sid, cvr_of_new_company, name_of_new_company, cur, grn_list = None):
    '''Creates a guarantee of a type to an existing trader and adds it to a list of guarantees if present'''
    while True:
        num = generate_random_grn()
        try:
            cur.execute(f'''insert into guarantee (grn     , type_cl          , customs_office_cl, trader_sid  , status_cl, acceptance_dt, reference_amount    ,currency_cl, access_code, monitor_type_cl, no_of_certificates, "version")
                            values		          ('{num}' , {guarantee_type} , 'DK005600'       , {trader_sid},'VALID'   , '2023-01-01' , 90000000000         , 'DKK'     , 1234       , 3              , 1                 , 0);''')
            print("sid: ", trader_sid, ". GRN type: ", guarantee_type, "GRN: ", num)
            if grn_list is None:
                pass
            else:
                grn_list = np.append(grn_list, num)
            break
        except:
            pass
    cur.execute(f'''insert into guarantor (grn    ,   tin                 , referenced,  name                  , country_cl, post_code, city , contact_person  , phone     , email , street_and_number)
                                 values   ('{num}', '{cvr_of_new_company}', false     , '{name_of_new_company}', 'DK'      , '1000'   , 'KBH', 'contact person', '12345678', 'mail', 'street 1');''')
    return grn_list
def generate_random_grn() -> str:
    '''Tis function generates a proper GRN for type 0 or type 1'''
    # Generate a random integer between 0 and 9999999 (inclusive)
    random_number = random.randint(0, 999999)

    # Convert the integer to a 7-digit string with leading zeroes
    random_string = str(random_number).zfill(6)
    # Append the string to "22DK005600"
    result = "22DK005600" + random_string
    result = result + str(calculate_check_digit(result))

    return result

def update_excel(array, excel_file_path, sheet_name, column_name):
    # Load the Excel file into a Pandas DataFrame
    df = pd.read_excel(excel_file_path, sheet_name=sheet_name)
    df_test = df[column_name].dropna().values
    # add the new guarantees to the existing ones in the dataframe
    new_column_0 = np.concatenate((df_test, array), axis=None)
    new_column_0_pd = pd.Series(new_column_0)
    # Append the array to the end of the specified column
    df[column_name] = new_column_0_pd
    for cell, n in zip(df['EORI number'], range(len(df['EORI number']))):
        df.loc[n, 'EORI number'] = load.make_CVR_EORI(int_to_string(cell))
    # Save the updated DataFrame to the Excel file
    df['Master Access Code'].fillna(1234, inplace=True)
    with pd.ExcelWriter(excel_file_path) as writer:
        df.to_excel(writer, sheet_name=sheet_name, index=False)

def int_to_string(value):
    if isinstance(value, int):
        return str(value)
    else:
        return value

def escape_single_quote(input_string):
    if "'" in input_string:
        # Using the replace method to add a backslash before the single quote
        escaped_string = input_string.replace("'", "''")
        return escaped_string
    else:
        # If no single quote is found, return the original string
        return input_string

def get_sid(EORI_number, cur) -> int:
    cur.execute(f'''
            SELECT sid 
            From trader
            where tin = '{EORI_number}' 
            ''')
    return cur.fetchall()[0][0]

if __name__ == "__main__":
    guarantee_0_1_trader_query()
    # val = get_sid('DK34461597', database_connection.connection(database_connection.tfe_gms_db).cursor())
    x = 2
    # print(escape_single_quote("Tests' ing"))
    # update_excel([1,2,3,4,], os.getcwd() + "\data\Firma garantier til fletning med breve Test.xlsx", 'Sheet1','Type 0 GRN')
    # print(generate_random_grn())

    # conn = database_connection.connection(database_connection.tfe_gms_db)
    # cur = conn.cursor()
    # execute_guarantee(1, 6, 13421730,"grn type 0 tester", cur)
    # conn.commit()