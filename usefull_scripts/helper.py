from datetime import datetime, timedelta
from move_sheets_excel import cursor, pack_out
import plotly.express as px
import pandas as pd
# def amount_declaration_progression(weeks_back):
#     for weeks in
#     # Hvor langt skal den gå tilbage? 8 uger? input

def amount_declarations_per_week(weeks):
    cur = cursor("tfe01_trader_portal")
    y_values = []
    for i in range(weeks):
        start_of_week = datetime.now() - timedelta(days=i*7+7)
        end_of_week = datetime.now()-timedelta(days=i*7)

        amount_declarations_sql = f'''SELECT *
            FROM sw_customs_message
            JOIN sw_cust_decl_proc ON sw_customs_message.custdeclaration_id  = sw_cust_decl_proc.id
            WHERE messagetype = 'DECLARATION'
            AND operator_id NOT IN ('13421730', '30808460', '13116482', 'swp.tdp01.b2b', 'tdp.export', 'swp.transit.agent', 'swp.ff.admin', '99999999')
            AND operator_id NOT LIKE '%19552101'
            AND procedure_category NOT IN ('H7', 'I2')
            AND submission_date > '{start_of_week}'
            AND submission_date < '{end_of_week}'
            '''

        cur.execute(amount_declarations_sql)
        amount_declaraions = pack_out(cur.fetchall())
        y_values.append(len(amount_declaraions))
        if i == 0:
            print("The past week: ", len(amount_declaraions))
        else:
            print(i, "to", i+1, "weeks ago: ", len(amount_declaraions))

    x_values = list(range(weeks))
    reversed_x_values = x_values[::-1]

    fig = px.line(x=x_values, y=y_values, markers=True, line_shape='linear', title='Chart over amount of declarations')

    fig.update_xaxes(title_text='Weeks ago')
    fig.update_yaxes(title_text='Declarations')
    fig.show()

if __name__ == '__main__':  
    amount_declarations_per_week(8)