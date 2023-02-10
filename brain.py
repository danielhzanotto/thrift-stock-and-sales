from tkinter import *
import pandas as pd
from random import randint
from tkinter import messagebox
from datetime import datetime as dt


class Brain:
    '''methods to manipulate data from estoque and categorias'''

    def __init__(self):
        pass

    def get_categorias_dict():
        '''pega as categorias e transforma em dicionário'''
        df = pd.read_excel("data.xlsx", sheet_name="categorias")
        dict_df = df.to_dict(orient='list')
        return {v[0]: [i for i in v[1] if str(i) != 'nan'] for v in dict_df.items()}

    def get_dados_dict():
        df = pd.read_excel("data.xlsx", sheet_name="dados")
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
        data_ = self.get_categorias_dict()
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
        data_info = self.get_categorias_dict()
        if pesquisa_info[0] == 1:
            df = df.loc[df["cod_venda"] == 0]
        elif pesquisa_info[0] == 2:
            df = df.loc[df["cod_venda"] != 0]

        for n in range(1, 5):
            if len(pesquisa_info[n]) != 0:
                ind_list = [list(data_info.values())[n][i]
                            for i in pesquisa_info[n]]
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
        df = self.get_categorias_dict()
        lista_index = str(indexes).strip().split(" ")
        return [df[lista].index(i) for i in lista_index]

    def checar_se_vendido(produto):
        df = pd.read_excel("data.xlsx", sheet_name="estoque")
        df.loc[df['cod'] == produto]
        return df['cod_venda'].values[0] != 0

    def continuar_cadastro(window, cod):
        return messagebox.askyesno(parent=window,
                                   title="Cadastro Feito!", message=f"Seu produto foi cadastrado com o código {cod}!\nGostaria de cadastrar outro produto?")

    def confirmar_editar(window):
        return messagebox.askyesno(parent=window,
                                   title="Confirmar edição", message=f"Você tem certeza que gostaria de editar esta peça?\nTodas as informações anteriores serão perdidas.")

    def categoria_em_branco(window, cod):
        return messagebox.showinfo(parent=window,
                                   title="Ooops!", message=f"Não deixe {cod} em branco!")

    def venda_invalido(window):
        return messagebox.showinfo(parent=window,
                                   title="Ooops!", message=f"Valor de venda inválido!\nFavor não deixar zerado, igual ou menor que o valor de compra.")

    def valor_invalido(window, cod):
        return messagebox.showinfo(parent=window,
                                   title="Ooops!", message=f"Valor de {cod} inválido...\nFavor informar {cod} válido!.")

    def confirmar_cancelar(window):
        return messagebox.askyesno(parent=window,
                                   title="Confirmar cancelamento", message=f"Você tem certeza que gostaria de cancelar?\nTodas as informações serão perdidas.")

    def pesquisa_vazia(window):
        return messagebox.showinfo(parent=window,
                                   title="Ooops!", message=f"Sua pesquisa não retornou resultado...\nConfira os filtros e tente novamente!.")

    def venda_realizada(window):
        return messagebox.showinfo(parent=window,
                                   title="Pronto!", message=f"Operação Realizada com Sucesso!\nO cupom logo será gerado")

    def produto_vendido(window):
        return messagebox.showinfo(parent=window,
                                   title="Ooops!", message=f"Parece que este produto já foi vendido!")

    def em_dev(window):
        return messagebox.showinfo(parent=window,
                                   title="Ooops!", message=f"Esta aplicação ainda está em desenvolvimento!\nAguarde os próximos capítulos")


class BrainVendas:
    def __init__(self) -> None:
        pass

    def gerar_cod_venda(self):
        cod = "V" + "-" + dt.today().strftime('%y-%m-%d') + "-" + str(randint(000, 999))
        cod_existe = self.checar_cod_venda_existe(self, cod)
        while cod_existe:
            cod = "V" + str(randint(00000, 99999))
            cod_existe = self.checar_cod_venda_existe(self, cod)
        return cod

    def checar_cod_venda_existe(self, codigo):
        df = pd.read_excel("data.xlsx", sheet_name="vendas")
        if codigo in list(df["cod_venda"]):
            return True
        elif codigo not in list(df["cod_venda"]):
            return False

    def pegar_produto_venda_code(code):
        produto = Brain.get_pesquisa_code(int(code))
        produto_dict = produto.to_dict(orient="list")
        produto_str = f"[{produto_dict['cod'][0]}]{produto_dict['categoria'][0]}: {produto_dict['desc'][0]}"
        produto_str_f = produto_str.ljust(
            52, "-") + f"R${produto_dict['valor_venda'][0]},00"
        return [code, produto_str_f, int(produto_dict['valor_venda'][0])]

    def pegar_nomes_metodos(coluna, index):
        df = pd.read_excel("data.xlsx", sheet_name="categorias")
        return df[coluna][index]

    def gerar_str_itens(lista):
        itens_str = ""
        for item in lista:
            itens_str += str(item) + " "
        return itens_str.strip()

    def gerar_venda(dict):
        df_estoque = pd.read_excel("data.xlsx", sheet_name="estoque")
        df_vendas = pd.read_excel("data.xlsx", sheet_name="vendas")
        teste_df = pd.DataFrame(dict, index=[0])

        df_vendas = pd.concat([df_vendas, teste_df], ignore_index=True)

        produtos = list(teste_df["itens"])[0].split(" ")
        for produto in produtos:
            df_estoque.loc[df_estoque['cod'] == int(
                produto), 'cod_venda'] = teste_df['cod_venda'].values[0]

        with pd.ExcelWriter("data.xlsx", mode="a", if_sheet_exists='overlay') as f:
            df_vendas.to_excel(f, sheet_name="vendas", index=False)
            df_estoque.to_excel(f, sheet_name="estoque", index=False)

    def pegar_dados_vazios(dados, coluna):
        if dados[coluna][0] != 0:
            return f"{coluna.title()}: {dados[coluna][0]}\n"
        else:
            return ""

    def gerar_cupom(self, infos, lista, dados):
        itens = ""
        for item in lista:
            itens += item + "\n"

        str_cnpj = self.pegar_dados_vazios(dados, 'cnpj')
        str_instagram = self.pegar_dados_vazios(dados, 'instagram')
        str_site = self.pegar_dados_vazios(dados, 'site')
        str_telefone = self.pegar_dados_vazios(dados, 'telefone')
        str_local = self.pegar_dados_vazios(dados, 'cidade')

        str_mensagem = ""
        if dados['mensagem'][0] != 0:
            str_mensagem = dados['mensagem'][0]

        str_nome = f"{str(dados['nome_fantasia'][0]).upper().ljust(44, ' ')}{str_cnpj}\n"

        str_divisor = "".ljust(60, "-") + "\n"
        str_total = 'Valor Produtos:'.ljust(
            52, " ") + f"R${int(infos['valor_total'])},00" + "\n"
        str_desconto = 'Valor Desconto:'.ljust(
            49, " ") + f" - R${int(infos['valor_desconto'])},00" + "\n"
        str_entrega = 'Valor Entrega:'.ljust(
            49, " ") + f" + R${int(infos['valor_entrega'])},00" + "\n"
        str_final = 'Valor Final:'.ljust(
            52, " ") + f"R${int(infos['valor_final'])},00" + "\n"

        comprovante = f"{str_nome}{str_instagram}{str_site}{str_telefone}{str_local}{str_divisor}{infos['nome_cliente']}\nCPF: {infos['cpf']}\n{infos['cidade']}-{infos['uf']}\n{str_divisor}\n{itens}\n{str_divisor}{str_total}{str_desconto}{str_entrega}{str_final}{str_divisor}{str_mensagem}\n{infos['data']}"

        with open(f"comprovantes/{infos['cod_venda']}.txt", 'w', encoding='utf-8') as f:
            f.write(comprovante)
