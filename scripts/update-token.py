import re
from pykeepass import PyKeePass
from pykeepass.exceptions import CredentialsError
from twill.commands import *
import pwinput


def open_keepass_db() -> PyKeePass:
    for i in range(3):
        try:
            password = pwinput.pwinput(prompt="Enter keepass password: ", mask='*')
            return PyKeePass('Database.kdbx', password=password)
        except CredentialsError as e:
            print('Invalid credentials.')
    exit('-1')


def update_kubernetes_token(keepass: PyKeePass):
    login_link = 'https://login.nonp.dmsnet.dk/login'
    go(login_link)
    fv("1", "login", "nc_jtf")
    fv("1", "password", keepass.find_entries(title='UFST-DMS NONProd', first=True).password)
    submit('0', 'None')

    html = browser.html
    token = re.search("--token='([^']*)'", html).group(1)

    with(open(r"C:\Users\jtf\OneDrive - Netcompany\config.txt")) as f:
        config_file_contents = f.read()

    with(open('config.txt', 'w')) as f:
        f.write(re.sub("token:[\n\r\s]+'[^']*'", f"token: '{token}'", config_file_contents))

    print("Updated token!")



update_kubernetes_token(keepass=open_keepass_db())
