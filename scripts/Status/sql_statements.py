amount_declarations_online_sql = f'''SELECT sw_cust_decl_proc.id, lrn, submission_date, operator_id 
FROM sw_customs_message
JOIN sw_cust_decl_proc ON sw_customs_message.custdeclaration_id  = sw_cust_decl_proc.id
WHERE messagetype LIKE 'DECLARATION'
  AND operator_id NOT IN ('13421730', '30808460', '13116482', 'swp.tdp01.b2b', 'tdp.export', 'swp.transit.agent', 'swp.ff.admin', '99999999') 
  AND operator_id NOT LIKE '%19552101' 
  AND procedure_category NOT IN ('H7', 'I2')
  AND operator_id LIKE '%:%'
  order by submission_date desc '''

amount_declarations_s2s_sql = f'''SELECT applicant_tin
FROM sw_customs_message
JOIN sw_cust_decl_proc ON sw_customs_message.custdeclaration_id  = sw_cust_decl_proc.id
WHERE messagetype LIKE 'DECLARATION'
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
where operator_id not in ('13421730', '30808460', '13116482', 'swp.tdp01.b2b', 'tdp.export', 'swp.transit.agent', 'swp.ff.admin', '99999999') 
and operator_id not like '%19552101' 
and procedure_category not in ('H7', 'I2')
--and called_by_rest_consumer = true '''

unique_s2s_operators_sql = f'''select distinct applicant_tin from sw_cust_decl_proc scdp
where operator_id not in ('13421730', '30808460', '13116482', 'swp.tdp01.b2b', 'tdp.export', 'swp.transit.agent', 'swp.ff.admin', '99999999') 
and operator_id not like '%19552101' 
and operator_id not like '%:%'
and procedure_category not in ('H7', 'I2')
--and called_by_rest_consumer = true '''

unique_online_operators_sql = f'''select distinct applicant_tin from sw_cust_decl_proc scdp
where operator_id not in ('13421730', '30808460', '13116482', 'swp.tdp01.b2b', 'tdp.export', 'swp.transit.agent', 'swp.ff.admin', '99999999') 
and operator_id not like '%19552101' 
and operator_id like '%:%'
and procedure_category not in ('H7', 'I2')
--and called_by_rest_consumer = 'false'
order by applicant_tin'''