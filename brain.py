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

    def gerar_genero(self, genero):
        if genero == 0:
            return "Feminino"
        elif genero == 1:
            return "Masculino"
        elif genero == 2:
            return "Unissex"

    def salvar_roupa(info):
        df = pd.read_excel("roupas.xlsx")
        roupa = pd.DataFrame(info, index=[0])
        df = pd.concat([df, roupa], ignore_index=True)
        df.to_excel("roupas.xlsx", index=False)

    def tuple_to_str(data):
        data_str = ""
        for i in data:
            data_str = data_str + " " + str(i)
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

    def pegar_tamanhos():
        df = pd.read_excel("roupas.xlsx")
        tamanhos = list(df["tamanho"])
        return list(set(tamanhos))

    def pegar_dia():
        return dt.today().strftime('%Y-%m-%d')