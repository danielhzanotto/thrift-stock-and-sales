from tkinter import *
import pandas as pd
from random import randint
from tkinter import messagebox
from datetime import datetime as dt


class Brain:
    def __init__(self):
        pass

    def get_data_dict():
        df = pd.read_excel("data.xlsx", sheet_name="categorias")
        dict_df = df.to_dict(orient='list')
        return {v[0]: [i for i in v[1] if str(i) != 'nan'] for v in dict_df.items()}

    def gerar_cod(self):
        cod = randint(00000, 99999)
        cod_existe = self.checar_cod_existe(self, cod)
        while cod_existe:
            cod = randint(00000, 99999)
            cod_existe = self.checar_cod_existe(self, cod)
        return cod

    def checar_cod_existe(self, codigo):
        df = pd.read_excel("data.xlsx", sheet_name="estoque")
        if codigo in list(df["cod"]):
            return True
        elif codigo not in list(df["cod"]):
            return False

    def salvar_roupa(info):
        df = pd.read_excel("data.xlsx", sheet_name="estoque")
        roupa = pd.DataFrame(info, index=[0])
        df = pd.concat([df, roupa], ignore_index=True)
        with pd.ExcelWriter("data.xlsx", mode="a", if_sheet_exists='overlay') as f:
            df.to_excel(f, sheet_name="estoque", index=False)

    def editar_roupa(info):
        df = pd.read_excel("data.xlsx", sheet_name="estoque")
        for key in info.keys():
            df.loc[df['cod'] == info['cod'], key] = info[key]
        with pd.ExcelWriter("data.xlsx", mode="a", if_sheet_exists='replace') as f:
            df.to_excel(f, sheet_name="estoque", index=False)

    def registrar_item(self, data, tipo):
        data_ = self.get_data_dict()
        data_str = ""
        for i in data:
            data_str += str(data_[tipo][int(i)]).title() + " "
        return data_str

    def preencher_vazio(cat):
        if len(cat) == 0:
            return "-"
        else:
            return cat.title()

    def pegar_dia():
        return dt.today().strftime('%Y-%m-%d')

    def get_pesquisa_code(code):
        df = pd.read_excel("data.xlsx", sheet_name="estoque")
        return df.loc[df["cod"] == int(code)]

    def df_to_dict(df):
        return df.to_dict(orient="list")

    def get_pesquisa_list(l, column, dataframe):
        counter = len(l)
        index = 0
        df_2 = dataframe.loc[dataframe["tamanho"] == "f"]
        while counter > 0:
            add_df = dataframe.loc[dataframe[column].str.contains(
                l[index].title())]
            df_2 = pd.concat([df_2, add_df], ignore_index=True)
            counter -= 1
            index += 1
        return df_2

    def get_pesquisa(self, pesquisa_info):
        df = pd.read_excel("data.xlsx", sheet_name="estoque")
        data_info = self.get_data_dict()

        if pesquisa_info[0] == 1:
            df = df.loc[df["data_saida"] != 0]
        elif pesquisa_info[0] == 2:
            df = df.loc[df["data_saida"] == 0]

        for n in range(1, 5):
            if len(pesquisa_info[n]) != 0:
                ind_list = [data_info[n][i] for i in pesquisa_info[n]]
                df = self.get_pesquisa_list(
                    ind_list, list(data_info.keys())[n], df)

        if len(pesquisa_info[5]) != 0:
            ind_list = pesquisa_info[5].split(" ")
            df = self.get_pesquisa_list(ind_list, "marca", df)

        if len(pesquisa_info[6]) != 0:
            ind_list = pesquisa_info[6].split(" ")
            df = self.get_pesquisa_list(ind_list, "desc", df)

        return df

    def lista_select(self, lista, indexes):
        df = self.get_data_dict()
        lista_index = str(indexes).strip().split(" ")
        return [df[lista].index(i) for i in lista_index]

    def continuar_cadastro(window, cod):
        return messagebox.askyesno(parent=window,
                                   title="Cadastro Feito!", message=f"Sua peça foi cadastrada com o código {cod}!\nGostaria de continuar cadastrando?")

    def confirmar_editar(window):
        return messagebox.askyesno(parent=window,
                                   title="Confirmar edição", message=f"Você tem certeza que gostaria de editar esta peça?\nTodas as informações anteriores serão perdidas.")

    def categoria_em_branco(window, cod):
        return messagebox.showinfo(parent=window,
                                   title="Ooops!", message=f"Não deixe {cod} em branco!")
