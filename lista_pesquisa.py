from tkinter import *


class ListaPesquisa:
    def __init__(self, init, info):
        self.init = init
        self.colors = self.init.brain.get_data(self)[2]

        self.roupas_pesquisa = info

        self.window_lista = Toplevel()
        self.window_lista.title("Resultado Pesquisa")
        self.window_lista.config(padx=20, pady=20, bg=self.colors[0])

        self.mensagem_resultado = Label(self.window_lista, text="Resultado da Pesquisa", font=(
            'Verdana', 16, "bold"), bg=self.colors[0], fg=self.colors[3])
        self.mensagem_resultado.grid(row=0, column=0, columnspan=4)

        self.divisor = Label(self.window_lista, text="____________________________\n", font=(
            'Verdana', 16, "bold"), bg=self.colors[0], fg=self.colors[3])
        self.divisor.grid(row=1, column=0, columnspan=4)

        resultado_var = Variable(value=self.criar_lista_roupas())
        self.resultado_lista = Listbox(
            master=self.window_lista, height=15, width=70, listvariable=resultado_var, fg=self.colors[4])
        self.resultado_lista.grid(row=2, column=0, columnspan=4)

        self.divisor2 = Label(self.window_lista, text="____________________________\n", font=(
            'Verdana', 16, "bold"), bg=self.colors[0], fg=self.colors[3])
        self.divisor2.grid(row=3, column=0, columnspan=4)

        self.cancelar_button = Button(
            self.window_lista, text="Cancelar", width=10, bg=self.colors[1], fg=self.colors[4], highlightthickness=0, font=('Verdana', 10), command=self.cancelar)
        self.cancelar_button.grid(row=4, column=0)

        self.editar_button = Button(self.window_lista, text="Editar", width=10, font=(
            'Verdana', 10), bg=self.colors[1], fg=self.colors[4], highlightthickness=0, command=self.editar_roupa)
        self.editar_button.grid(row=4, column=1)

        self.adicionar_button = Button(self.window_lista, text="Editar", font=(
            'Verdana', 10), bg=self.colors[1], fg=self.colors[4], width=30, highlightthickness=0, command=self.adicionar_venda)
        self.adicionar_button.grid(row=4, column=2, columnspan=2)

        self.window_lista.mainloop()

    def cancelar(self):
        self.window_lista.destroy()

    def editar_roupa(self):
        pass

    def adicionar_venda(self):
        pass

    def criar_lista_roupas(self):
        return 0
