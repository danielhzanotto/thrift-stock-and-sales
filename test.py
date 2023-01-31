import pandas as pd


def get_pesquisa_code(code):
    df = pd.read_excel("roupas.xlsx")
    print(df.loc[df["cod"] == 99265])


get_pesquisa_code(45104)
