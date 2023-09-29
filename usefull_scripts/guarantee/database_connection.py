import psycopg2

tfe_gms_db = "tfe01_gms_guarantee_management"
sit05_gms_db = "sit05_gms_guarantee_management"
sit05_trader_portal = "sit05_trader_portal"
tfe01_trader_portal = "tfe01_trader_portal"
sit_05_import_work_task = "sit05_cwm_import_work_task_manager"
tfe01_add_msg = "tfe01_cwm_import_additional_message"
tfe_work_task = "tfe01_platform_work_task_manager"

def cursor(database):
    # write your UFST-DMS NONProd credentials
    # replace with lq creds
    username = "nc_jtf"
    password = "uPf4vMRVt7K*4st7"
    conn = psycopg2.connect(
        host="127.129.224.100",
        database=database,
        user=username,
        password=password
    )
    return conn.cursor()

def connection(database):
    # write your UFST-DMS NONProd credentials
    username = "nc_jtf"
    password = "uPf4vMRVt7K*4st7"
    conn = psycopg2.connect(
        host="127.129.224.100",
        database=database,
        user=username,
        password=password
    )
    return conn