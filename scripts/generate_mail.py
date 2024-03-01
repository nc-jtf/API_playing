import pandas as pd
import os
import clipboard

def create_mail(EORI = None, Email = None):
    df = pd.read_excel("C:/Users/jtf/PycharmProjects/API_playing/scripts/guarantee/data/Firma garantier til fletning med breve Test.xlsx", sheet_name='Sheet1')

    if Email is not None:
        row = df[df['E-mail'] == Email]

    if EORI is not None:
        row = df[df['EORI number'] == EORI]

    # Extract values for "Firma", "New Type 0 GRN", and "New Type 1 GRN"
    result = {
        'Firma': row['Firma'].values[0],
        'New Type 0 GRN': row['New Type 0 GRN'].values[0],
        'New Type 1 GRN': row['New Type 1 GRN'].values[0]}
    firma = result.get("Firma")
    mail = f'''Kære {result.get("Firma")},
grundet en systemopdatering er vi nødsaget til at lave nye garantier til jeres testning. De følgende garantier er blevet lavet på TFE og skal bruges fremadrettet:
Type 0: {result.get("New Type 0 GRN")}
Type 1: {result.get("New Type 1 GRN")}
Vi beklager for ulejligheden
Venlig hilsen,
DMS Onboarding team'''
    clipboard.copy(mail)
    return mail

if __name__ == "__main__":
    print(create_mail(Email="karstenfrederiksen@gmail.com"))
    # print(create_mail(EORI="DK42140015"))
    # print(os.listdir("C:/Users/jtf/PycharmProjects/API_playing/scripts/guarantee/data"))