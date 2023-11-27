from scripts.database_connection import cursor
import plotly.graph_objects as go
from amount_declarations_per_week import *
import re
from sql_statements import *

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

cur = cursor("tfe01_trader_portal")

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

    #finder gengående firmaer
    online_companies = set(re.search(r':(\d{8})$', s).group(1) for s in unique_online_operators if re.search(r':(\d{8})$', s))
    s2s_companies_set = set(unique_s2s_operators)
    common_elements = online_companies.intersection(s2s_companies_set)
    overlap = len(common_elements)

    print("amount of online declarations: ", len(amount_declarations_online))
    print("amount of s2s declarations: ", len(amount_declarations_s2s))
    print("Amount of online operators: ", len(online_companies)-overlap)
    print("Amount of s2s operators: ", len(unique_s2s_operators))