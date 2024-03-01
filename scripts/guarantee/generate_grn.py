import os
import random
import string
import pandas as pd


def generate_grn_from_rule(year, country_code, voucher):
    # Extract last two digits of the year
    year_last_two_digits = str(year)[-2:]

    # Generate a unique identifier (12 alphanumeric characters)
    unique_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=12))

    # Generate a check digit (a single numeric digit
    #TODO: split according to rules
    check_digit = str(random.randint(0, 9))

    # Combine all parts
    grn = year_last_two_digits + country_code + unique_id + check_digit + voucher

    return grn.upper()

def calculate_check_digit(grn) -> int:
    grn = grn[:16]
    letters = {
        'A': 10, 'B': 12, 'C': 13, 'D': 14, 'E': 15, 'F': 16, 'G': 17, 'H': 18, 'I': 19, 'J': 20,
        'K': 21, 'L': 23, 'M': 24, 'N': 25, 'O': 26, 'P': 27, 'Q': 28, 'R': 29, 'S': 30, 'T': 31,
        'U': 32, 'V': 34, 'W': 35, 'X': 36, 'Y': 37, 'Z': 38
    }
    grn = [int(char) if char.isdigit() else letters[char] for char in grn]

    total_sum = 0
    for i, num in enumerate(grn):
        total_sum += num * 2**i

    check_digit = total_sum % 11
    if check_digit == 10:
        check_digit = 0

    return check_digit
def get_GRNs(excel_file_path, sheet_name, column_name):
    # Load the Excel file into a Pandas DataFrame
    df = pd.read_excel(excel_file_path, sheet_name=sheet_name)
    df_coulumn = df[column_name].dropna().values
    # for GRN in df_coulumn:
    #     if(calculate_check_digit(GRN[:-1]) != GRN[-1]):
    #         GRN[-1] = calculate_check_digit(GRN[:-1])

    for i, GRN in enumerate(df[column_name]):
        calculated_check_digit = calculate_check_digit(GRN[:-1])
        if calculated_check_digit != GRN[-1]:
            # Update the last character in the DataFrame
            df.at[i, column_name] = GRN[:-1] + str(calculated_check_digit)
    # calculate the proper GRN and
    # put it in the cell 2 to the left.
    #
    # do this for both couloumns (type 0 and 1)
    with pd.ExcelWriter(excel_file_path) as writer:
        df.to_excel(writer, sheet_name=sheet_name, index=False)
    print(df_coulumn)

if __name__ == '__main__':
    print(calculate_check_digit("22DK005600560978".upper()))
    # get_GRNs(os.getcwd() + "\data\Firma garantier til fletning med breve Test.xlsx", 'Sheet1','Type 0 GRN')
# print(generate_grn_from_rule(2023, 'IT', 'A001017'))
