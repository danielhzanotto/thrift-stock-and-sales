from tkinter import *


class ListaPesquisa:
    def __init__(self):
        pass

    def criar_lista(self, info, window):
        self.roupas_pesquisa = info
        self.mensagem_resultado = Label(master=window, text="Resultado da Pesquisa", font=(
            'Verdana', 16, "bold"), bg=self.colors[0], fg=self.colors[3])
        self.mensagem_resultado.grid(row=0, column=6, columnspan=4)

        self.divisor = Label(master=window, text="____________________________\n", font=(
            'Verdana', 16, "bold"), bg=self.colors[0], fg=self.colors[3])
        self.divisor.grid(row=2, column=6, columnspan=4)

        resultado_var = Variable(
            value=self.lista_pesquisa.criar_lista_roupas(self))
        self.resultado_lista = Listbox(
            master=window, height=18, width=70, listvariable=resultado_var, fg=self.colors[4])
        self.resultado_lista.grid(row=3, column=6, columnspan=4, rowspan=9)

        self.divisor2 = Label(master=window, text="____________________________\n", font=(
            'Verdana', 16, "bold"), bg=self.colors[0], fg=self.colors[3])
        self.divisor2.grid(row=12, column=6, columnspan=4)

        self.editar_button = Button(master=window, text="Abrir Info e Editar", width=23, font=(
            'Verdana', 10), bg=self.colors[1], fg=self.colors[4], highlightthickness=0, command=self.editar_roupa)

        self.adicionar_button = Button(master=window, text="Adicionar Produto à Venda", font=(
            'Verdana', 10), bg=self.colors[1], fg=self.colors[4], width=30, highlightthickness=0, command=self.adicionar_venda)

        if self.metodo == 'pesquisa':
            self.editar_button.grid_forget()
            self.adicionar_button.grid_forget()
            self.editar_button.grid(row=13, column=6, columnspan=2)
            self.adicionar_button.grid(row=13, column=8, columnspan=2)
        elif self.metodo == 'venda':
            self.editar_button.grid_forget()
            self.adicionar_button.grid_forget()
            self.adicionar_button.grid(row=13, column=8, columnspan=2)

    def criar_lista_roupas(self):
        return [f"[{roupa[1]}] {roupa[3]} ({roupa[4]}): {roupa[2]}" for roupa in self.roupas_pesquisa.itertuples()]
