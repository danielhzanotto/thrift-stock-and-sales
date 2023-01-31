from tkinter import *
import pandas as pd
from random import randint
from tkinter import messagebox
from datetime import datetime as dt


class Brain:
    def __init__(self):
        pass

    def get_data(self):
        df = pd.read_json("data.json", typ='series')
        return [categoria for categoria in df]

    def gerar_cod(self):
        cod = randint(00000, 99999)
        cod_existe = self.checar_cod_existe(self, cod)
        while cod_existe:
            cod = randint(00000, 99999)
            cod_existe = self.checar_cod_existe(self, cod)
        return cod

    def checar_cod_existe(self, codigo):
        df = pd.read_excel("roupas.xlsx")
        if codigo in list(df["cod"]):
            return True
        elif codigo not in list(df["cod"]):
            return False

    def salvar_roupa(info):
        df = pd.read_excel("roupas.xlsx")
        roupa = pd.DataFrame(info, index=[0])
        df = pd.concat([df, roupa], ignore_index=True)
        df.to_excel("roupas.xlsx", index=False)

    def registrar_cor(data):
        data_json = pd.read_json("data.json", typ='series')
        data_str = ""
        for i in data:
            data_str = data_str + " " + data_json[0][int(i)].title()
        return data_str

    def registrar_tamanho(data):
        data_json = pd.read_json("data.json", typ='series')
        data_str = ""
        for i in data:
            data_str = data_str + " " + data_json[4][int(i)].title()
        return data_str

    def continuar_cadastro(window, cod):
        return messagebox.askyesno(parent=window,
                                   title="Cadastro Feito!", message=f"Sua peça foi cadastrada com o código {cod}!\nGostaria de continuar cadastrando?")

    def categoria_em_branco(window, cod):
        return messagebox.showinfo(parent=window,
                                   title="Ooops!", message=f"Não deixe {cod} em branco!")

    def preencher_vazio(cat):
        if len(cat) == 0:
            return "-"
        else:
            return cat.title()

    def pegar_dia():
        return dt.today().strftime('%Y-%m-%d')

    def pegar_marcas():
        df = pd.read_excel("roupas.xlsx")
        return list(set(df["marca"]))

    def get_pesquisa_code(code):
        df = pd.read_excel("roupas.xlsx")
        return df.loc[df["cod"] == int(code)]

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
        df = pd.read_excel("roupas.xlsx")
        data_info = pd.read_json("data.json", typ='series')

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
