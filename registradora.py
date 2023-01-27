from tkinter import *


class Registradora:

    def __init__(self, init):
        self.init = init
        self.colors = self.init.brain.get_data(self)[2]

        self.window_register = Toplevel()
        self.window_register.title("Registrar Peça")
        self.window_register.config(padx=20, pady=20, bg=self.colors[0])

        self.mensagem_inicio = Label(self.window_register, text="Insira os dados da peça", font=(
            'Verdana', 16, "bold"), bg=self.colors[0], fg=self.colors[3])
        self.mensagem_inicio.grid(row=0, column=0, columnspan=4)

        self.divisor = Label(self.window_register, text="__________________________\n", font=(
            'Verdana', 16, "bold"), bg=self.colors[0], fg=self.colors[3])
        self.divisor.grid(row=1, column=0, columnspan=4)

        self.descrição_geral_label = Label(self.window_register, text="Descrição:", font=(
            'Verdana', 9, "bold"), bg=self.colors[0], fg=self.colors[3])
        self.descrição_geral_label.grid(row=2, column=0)
        self.descrição_geral_entrada = Entry(
            self.window_register, fg=self.colors[4], width=47)
        self.descrição_geral_entrada.grid(row=2, column=1, columnspan=3)

        self.marca_label = Label(self.window_register, text="Marca:", font=(
            'Verdana', 9, "bold"), bg=self.colors[0], fg=self.colors[3])
        self.marca_label.grid(row=3, column=0)
        self.marca_entrada = Entry(
            self.window_register, fg=self.colors[4], width=47)
        self.marca_entrada.grid(row=3, column=1, columnspan=3)

        self.tamanho_label = Label(self.window_register, text="Tamanho:", font=(
            'Verdana', 9, "bold"), bg=self.colors[0], fg=self.colors[3])
        self.tamanho_label.grid(row=4, column=0)
        self.tamanho_entrada = Entry(
            self.window_register, fg=self.colors[4], width=17)
        self.tamanho_entrada.grid(row=4, column=1)

        self.valor_compra_label = Label(self.window_register, text="Valor Compra:", font=(
            'Verdana', 9, "bold"), bg=self.colors[0], fg=self.colors[3])
        self.valor_compra_label.grid(row=5, column=0)
        self.valor_compra_entrada = Entry(
            self.window_register, fg=self.colors[4], width=17)
        self.valor_compra_entrada.grid(row=5, column=1)

        self.valor_venda_label = Label(self.window_register, text="Valor Venda:", font=(
            'Verdana', 9, "bold"), bg=self.colors[0], fg=self.colors[3])
        self.valor_venda_label.grid(row=6, column=0)
        self.valor_venda_entrada = Entry(
            self.window_register, fg=self.colors[4], width=17)
        self.valor_venda_entrada.grid(row=6, column=1)

        self.genero_label = Label(self.window_register, text="Genero:", font=(
            'Verdana', 9, "bold"), bg=self.colors[0], fg=self.colors[3])
        self.genero_label.grid(row=4, column=2)
        self.radio_state = IntVar()
        self.radio_genero0 = Radiobutton(
            self.window_register, text="Feminino", bg=self.colors[0], value=0, variable=self.radio_state)
        self.radio_genero1 = Radiobutton(
            self.window_register, text="Masculino", bg=self.colors[0], value=1, variable=self.radio_state)
        self.radio_genero2 = Radiobutton(
            self.window_register, text="Unissex", bg=self.colors[0], value=2, variable=self.radio_state)
        self.radio_genero0.grid(row=4, column=3)
        self.radio_genero1.grid(row=5, column=3)
        self.radio_genero2.grid(row=6, column=3)

        self.vazio_label = Label(self.window_register, text="\n", font=(
            'Verdana', 6), bg=self.colors[0], fg=self.colors[3])
        self.vazio_label.grid(row=7, column=0, columnspan=4)

        self.cores_label = Label(self.window_register, text="Cor:", font=(
            'Verdana', 9, "bold"), bg=self.colors[0], fg=self.colors[3])
        self.cores_label.grid(row=8, column=0, columnspan=2)
        cores_var = Variable(value=self.init.brain.get_data(self)[0])
        self.cores_lista = Listbox(
            master=self.window_register, height=8, width=20, listvariable=cores_var, selectmode=MULTIPLE, fg=self.colors[4], exportselection=0)
        self.cores_lista.grid(row=9, column=0, columnspan=2)

        self.categoria_label = Label(self.window_register, text="Categoria:", font=(
            'Verdana', 9, "bold"), bg=self.colors[0], fg=self.colors[3])
        self.categoria_label.grid(row=8, column=2, columnspan=2)
        categorias_var = Variable(value=self.init.brain.get_data(self)[1])
        self.categoria_lista = Listbox(
            master=self.window_register, height=8, width=20, listvariable=categorias_var, fg=self.colors[4], exportselection=0)
        self.categoria_lista.grid(row=9, column=2, columnspan=2)

        self.divisor = Label(self.window_register, text="__________________________\n", font=(
            'Verdana', 16, "bold"), bg=self.colors[0], fg=self.colors[3])
        self.divisor.grid(row=10, column=0, columnspan=4)

        self.cancelar_button = Button(
            self.window_register, text="Cancelar", width=12, bg=self.colors[1], fg=self.colors[4], highlightthickness=0, font=('Verdana', 10), command=self.cancelar)
        self.cancelar_button.grid(row=11, column=0)

        self.registrar_button = Button(
            self.window_register, text="Registrar Peça", width=37, bg=self.colors[1], fg=self.colors[4], highlightthickness=0, font=('Verdana', 10), command=self.salvar_conteudo)
        self.registrar_button.grid(row=11, column=1, columnspan=3)

        self.window_register.mainloop()

    def salvar_conteudo(self):
        self.code = self.init.brain.gerar_cod(self.init.brain)
        if self.checar_vazio():
            self.piece = {"cod": self.code,
                          "desc": self.descrição_geral_entrada.get().title(),
                          "categoria": self.categoria_lista.get(self.categoria_lista.curselection()).title(),
                          "tamanho": self.init.brain.preencher_vazio(self.tamanho_entrada.get()),
                          "genero": self.init.brain.gerar_genero(self, self.radio_state.get()),
                          "marca": self.init.brain.preencher_vazio(self.marca_entrada.get()),
                          "cor": self.init.brain.tuple_to_str(self.cores_lista.curselection()),
                          "valor_compra": self.valor_compra_entrada.get(),
                          "valor_venda": self.init.brain.preencher_vazio(self.valor_venda_entrada.get()),
                          "data_entrada": self.init.brain.pegar_dia(),
                          "data_saida": 0
                          }
            self.init.brain.salvar_roupa(self.piece)
            continuar = self.init.brain.continuar_cadastro(
                self.window_register, self.code)

            if continuar:
                self.descrição_geral_entrada.delete(0, END)
                self.marca_entrada.delete(0, END)
                self.tamanho_entrada.delete(0, END)
                self.valor_compra_entrada.delete(0, END)
                self.valor_venda_entrada.delete(0, END)
                self.radio_genero0.select()
                self.cores_lista.selection_clear(0, END)
                self.categoria_lista.selection_clear(0, END)
                self.window_register.update()
            else:
                self.window_register.destroy()

    def cancelar(self):
        self.window_register.destroy()

    def checar_vazio(self):
        self.categoria_vazia = ""
        if len(self.descrição_geral_entrada.get()) == 0:
            self.categoria_vazia = "Descrição"
        elif len(self.categoria_lista.curselection()) == 0:
            self.categoria_vazia = "Categoria"
        elif len(self.cores_lista.curselection()) == 0:
            self.categoria_vazia = "Cor"
        elif self.valor_compra_entrada.get() == 0:
            self.categoria_vazia = "Valor de Compra"

        if self.categoria_vazia == "":
            return True
        else:
            self.init.brain.categoria_em_branco(
                self.window_register, self.categoria_vazia)
            return False
