import pandas as pd


df = pd.read_excel("data.xlsx", sheet_name="categorias")
print(df["tipo_entrega"][3])
