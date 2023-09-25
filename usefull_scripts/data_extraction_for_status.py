from move_sheets_excel import cursor, pack_out
# import matplotlib.pyplot as plt
import plotly.graph_objects as go
from helper import *

def plot_pie_chart_plotly(data_dict):
    labels = list(data_dict.keys())
    values = list(data_dict.values())

    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])

    fig.update_layout(
        title='Procedure category split',
        autosize=False,
        width=600,
        height=600
    )
    fig.show()

def count_unique_elements(input_list):
    unique_elements = {}

    for item in input_list:
        if item in unique_elements:
            unique_elements[item] += 1
        else:
            unique_elements[item] = 1

    return unique_elements

def rejection_rate(cursor):
    cur.execute('''SELECT *
    from sw_customs_message
    WHERE messagetype = '03'
    AND ownerid NOT IN ('13421730', '30808460', '13116482', 'swp.tdp01.b2b', 'tdp.export', 'swp.transit.agent', 'swp.ff.admin', '99999999')
    AND operator_id NOT LIKE '%19552101
    ''')
    number_rejections = len(cur.fetchall())



cur = cursor("tfe01_trader_portal")

# sql
amount_declarations_online_sql = f'''SELECT sw_cust_decl_proc.id, lrn, submission_date, operator_id 
FROM sw_customs_message
JOIN sw_cust_decl_proc ON sw_customs_message.custdeclaration_id  = sw_cust_decl_proc.id
WHERE called_by_rest_consumer = false  
  AND messagetype LIKE 'DECLARATION'
  AND operator_id NOT IN ('13421730', '30808460', '13116482', 'swp.tdp01.b2b', 'tdp.export', 'swp.transit.agent', 'swp.ff.admin', '99999999') 
  AND operator_id NOT LIKE '%19552101' 
  AND procedure_category NOT IN ('H7', 'I2')
  AND operator_id LIKE '%:%'
  order by submission_date desc '''

amount_declarations_s2s_sql = f'''SELECT applicant_tin
FROM sw_customs_message
JOIN sw_cust_decl_proc ON sw_customs_message.custdeclaration_id  = sw_cust_decl_proc.id
WHERE called_by_rest_consumer = true 
  AND messagetype LIKE 'DECLARATION'
  AND operator_id NOT IN ('13421730', '30808460', '13116482', 'swp.tdp01.b2b', 'tdp.export', 'swp.transit.agent', 'swp.ff.admin', '99999999') 
  AND operator_id NOT LIKE '%19552101' 
  AND procedure_category NOT IN ('H7', 'I2')
  AND operator_id NOT LIKE '%:%' '''

procedure_categories_sql = f'''SELECT procedure_category 
FROM sw_customs_message
JOIN sw_cust_decl_proc ON sw_customs_message.custdeclaration_id  = sw_cust_decl_proc.id
  WHERE operator_id NOT IN ('13421730', '30808460', '13116482', 'swp.tdp01.b2b', 'tdp.export', 'swp.transit.agent', 'swp.ff.admin', '99999999') 
  AND operator_id NOT LIKE '%19552101' 
  AND messagetype LIKE 'DECLARATION'
  AND procedure_category NOT IN ('H7', 'I2') '''

amount_rejections_sql = f'''SELECT *
    FROM sw_customs_message
    JOIN sw_cust_decl_proc ON sw_customs_message.custdeclaration_id  = sw_cust_decl_proc.id
    WHERE messagetype = '03' -- antallet af errors for import/export
    AND operator_id NOT IN ('13421730', '30808460', '13116482', 'swp.tdp01.b2b', 'tdp.export', 'swp.transit.agent', 'swp.ff.admin', '99999999')
    AND operator_id NOT LIKE '%19552101'
    '''
amount_declarations_sql = f'''SELECT *
    FROM sw_customs_message
    JOIN sw_cust_decl_proc ON sw_customs_message.custdeclaration_id  = sw_cust_decl_proc.id
    WHERE messagetype = 'DECLARATION'
    AND operator_id NOT IN ('13421730', '30808460', '13116482', 'swp.tdp01.b2b', 'tdp.export', 'swp.transit.agent', 'swp.ff.admin', '99999999')
    AND operator_id NOT LIKE '%19552101'
    AND procedure_category NOT IN ('H7', 'I2')
    '''
unique_operators_sql = f'''select distinct applicant_tin from sw_cust_decl_proc scdp
where called_by_rest_consumer = true 
and operator_id not in ('13421730', '30808460', '13116482', 'swp.tdp01.b2b', 'tdp.export', 'swp.transit.agent', 'swp.ff.admin', '99999999') 
and operator_id not like '%19552101' 
and procedure_category not in ('H7', 'I2')'''

unique_s2s_operators_sql = f'''select distinct applicant_tin from sw_cust_decl_proc scdp
where called_by_rest_consumer = true 
and operator_id not in ('13421730', '30808460', '13116482', 'swp.tdp01.b2b', 'tdp.export', 'swp.transit.agent', 'swp.ff.admin', '99999999') 
and operator_id not like '%19552101' 
and operator_id not like '%:%'
and procedure_category not in ('H7', 'I2')'''

unique_online_operators_sql = f'''select distinct applicant_tin from sw_cust_decl_proc scdp
where called_by_rest_consumer = true 
and operator_id not in ('13421730', '30808460', '13116482', 'swp.tdp01.b2b', 'tdp.export', 'swp.transit.agent', 'swp.ff.admin', '99999999') 
and operator_id not like '%19552101' 
and operator_id like '%:%'
and procedure_category not in ('H7', 'I2')'''
if __name__ == '__main__':
    cur.execute(amount_declarations_online_sql)
    amount_declarations_online = pack_out(cur.fetchall())
    cur.execute(amount_declarations_s2s_sql)
    amount_declarations_s2s = pack_out(cur.fetchall())
    cur.execute(procedure_categories_sql)
    procedure_categories = pack_out(cur.fetchall())
    cur.execute(amount_rejections_sql)
    amount_rejections = pack_out(cur.fetchall())
    cur.execute(amount_declarations_sql)
    amount_declaraions = pack_out(cur.fetchall())
    cur.execute(unique_operators_sql)
    unique_operators = pack_out(cur.fetchall())
    cur.execute(unique_s2s_operators_sql)
    unique_s2s_operators = pack_out(cur.fetchall())
    cur.execute(unique_online_operators_sql)
    unique_online_operators = pack_out(cur.fetchall())
    cur.close()

    print("amount of online declarations: ", len(amount_declarations_online))
    print("amount of s2s declarations: ", len(amount_declarations_s2s))
    print("procedure category split: ", count_unique_elements(procedure_categories))
    print("Rejections: ",len(amount_rejections),"| Declarations: ",len(amount_declaraions),"| Percentage of declarations getting rejected: ",len(amount_rejections)/len(amount_declaraions)*100,"%")
    # print("Unique of S2S operators: ", unique_operators)
    print("Amount of online operators: ", len(unique_online_operators))
    print("Amount od s2s operators: ", len(unique_s2s_operators))
    # plot_pie_chart_plotly(count_unique_elements(procedure_categories))
    amount_declarations_per_week(8)



    #Tag deklerationer fra den sidste uge
    