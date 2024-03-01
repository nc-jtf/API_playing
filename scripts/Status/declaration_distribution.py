from amount_declarations_per_week import *

def Sort_Tuple(tup):
    # getting length of list of tuples
    lst = len(tup)
    for i in range(0, lst):

        for j in range(0, lst - i - 1):
            if (tup[j][1] > tup[j + 1][1]):
                temp = tup[j]
                tup[j] = tup[j + 1]
                tup[j + 1] = temp
    return tup


cur = cursor("tfe01_trader_portal")

unique_operators_sql = f'''select distinct operator_id from sw_cust_decl_proc scdp
where operator_id not in ('13421730', '30808460', '13116482', 'swp.tdp01.b2b', 'tdp.export', 'swp.transit.agent', 'swp.ff.admin', '99999999') 
and operator_id not like '%19552101' 
and procedure_category not in ('H7', 'I2')
and called_by_rest_consumer = true 
order by applicant_tin asc'''
# Hvis man har"called_by_rest_consumer" = true så tager den ikke online med, så hvis en EO kun bruger online er det misvisende
cur.execute(unique_operators_sql)
unique_operators = pack_out(cur.fetchall())
operator_dict = {}
operator_list = []
for operator in unique_operators:
    find_declarations_for_EO_sql = f'''SELECT sw_cust_decl_proc.id, lrn, submission_date, operator_id 
    FROM sw_customs_message
    JOIN sw_cust_decl_proc ON sw_customs_message.custdeclaration_id  = sw_cust_decl_proc.id
    WHERE called_by_rest_consumer = false  
        AND messagetype LIKE 'DECLARATION'
        AND operator_id IN ('{operator}') 
        AND procedure_category NOT IN ('H7', 'I2')
    order by submission_date desc '''


    cur.execute(find_declarations_for_EO_sql)
    fetched = cur.fetchall()
    if len(fetched) > 0:
        operator_dict[operator] = len(fetched)
        operator_list.append(cur.fetchall())
    # print(f"Amount of declarations for {operator}: ", len(declarations))

sorted_operator = sorted(operator_dict, key=lambda item: item[1], reverse=True)
print(operator_dict)
dict(sorted(operator_dict.items(), key=lambda item: item[1], reverse=False))

print(operator_dict)