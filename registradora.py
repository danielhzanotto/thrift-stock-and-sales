from tkinter import *


class Registradora:

    def __init__(self, init, metodo, roupa):
        self.init = init
        self.colors = self.init.brain.get_data_dict()['cores_programa']

        self.metodo = metodo
        self.roupa = roupa

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

        self.valor_compra_label = Label(self.window_register, text="Valor Compra:", font=(
            'Verdana', 9, "bold"), bg=self.colors[0], fg=self.colors[3])
        self.valor_compra_label.grid(row=4, column=0)
        self.valor_compra_entrada = Entry(
            self.window_register, fg=self.colors[4], width=13)
        self.valor_compra_entrada.grid(row=4, column=1)

        self.valor_venda_label = Label(self.window_register, text="Valor Venda:", font=(
            'Verdana', 9, "bold"), bg=self.colors[0], fg=self.colors[3])
        self.valor_venda_label.grid(row=4, column=2)
        self.valor_venda_entrada = Entry(
            self.window_register, fg=self.colors[4], width=13)
        self.valor_venda_entrada.grid(row=4, column=3)

        self.vazio_label = Label(self.window_register, text="\n", font=(
            'Verdana', 6), bg=self.colors[0], fg=self.colors[3])
        self.vazio_label.grid(row=5, column=2, columnspan=2)

        self.tamanho_label = Label(self.window_register, text="Tamanho:", font=(
            'Verdana', 9, "bold"), bg=self.colors[0], fg=self.colors[3])
        self.tamanho_label.grid(row=6, column=0, columnspan=2)
        tamanhos_var = Variable(
            value=self.init.brain.get_data_dict()['tamanho'])
        self.tamanhos_lista = Listbox(
            master=self.window_register, height=4, width=20, selectmode=MULTIPLE, listvariable=tamanhos_var, fg=self.colors[4], exportselection=0)
        self.tamanhos_lista.grid(row=7, column=0, columnspan=2)

        self.genero_label = Label(self.window_register, text="Genero:", font=(
            'Verdana', 9, "bold"), bg=self.colors[0], fg=self.colors[3])
        self.genero_label.grid(row=6, column=2, columnspan=2)
        generos_var = Variable(value=self.init.brain.get_data_dict()['genero'])
        self.genero_lista = Listbox(
            master=self.window_register, height=4, width=20, listvariable=generos_var, fg=self.colors[4], exportselection=0)
        self.genero_lista.grid(row=7, column=2, columnspan=2)

        self.cores_label = Label(self.window_register, text="Cor:", font=(
            'Verdana', 9, "bold"), bg=self.colors[0], fg=self.colors[3])
        self.cores_label.grid(row=9, column=0, columnspan=2)
        cores_var = Variable(value=self.init.brain.get_data_dict()['cor'])
        self.cores_lista = Listbox(
            master=self.window_register, height=8, width=20, listvariable=cores_var, selectmode=MULTIPLE, fg=self.colors[4], exportselection=0)
        self.cores_lista.grid(row=10, column=0, columnspan=2)

        self.categoria_label = Label(self.window_register, text="Categoria:", font=(
            'Verdana', 9, "bold"), bg=self.colors[0], fg=self.colors[3])
        self.categoria_label.grid(row=9, column=2, columnspan=2)
        categorias_var = Variable(
            value=self.init.brain.get_data_dict()['categoria'])
        self.categoria_lista = Listbox(
            master=self.window_register, height=8, width=20, listvariable=categorias_var, fg=self.colors[4], exportselection=0)
        self.categoria_lista.grid(row=10, column=2, columnspan=2)

        self.divisor = Label(self.window_register, text="__________________________\n", font=(
            'Verdana', 16, "bold"), bg=self.colors[0], fg=self.colors[3])
        self.divisor.grid(row=11, column=0, columnspan=4)

        self.cancelar_button = Button(
            self.window_register, text="Cancelar", width=12, bg=self.colors[1], fg=self.colors[4], highlightthickness=0, font=('Verdana', 10), command=self.cancelar)
        self.cancelar_button.grid(row=12, column=0)

        self.registrar_button = Button(
            self.window_register, text="Registrar Peça", width=37, bg=self.colors[1], fg=self.colors[4], highlightthickness=0, font=('Verdana', 10), command=self.salvar_conteudo)
        self.registrar_button.grid(row=12, column=1, columnspan=3)

        if self.metodo == 'editor':
            self.descrição_geral_entrada.insert(
                index=0, string=self.roupa["desc"][0])
            self.marca_entrada.insert(index=0, string=self.roupa["marca"][0])
            self.valor_compra_entrada.insert(
                index=0, string=self.roupa["valor_compra"][0])
            self.valor_venda_entrada.insert(
                index=0, string=self.roupa["valor_venda"][0])

            self.checked_state = IntVar()
            self.see_password = Checkbutton(self.window_register,  bg=self.colors[0], fg=self.colors[3],
                                            text="Ver valor de compra", variable=self.checked_state, command=self.checkbutton_see)
            self.see_password.grid(row=5, column=0, columnspan=2)

            self.vender_button = Button(
                self.window_register, text="Iniciar Venda", width=25, bg=self.colors[1], fg=self.colors[4], highlightthickness=0, font=('Verdana', 10), command=self.iniciar_venda)
            self.vender_button.grid(row=13, column=0, columnspan=4)

            self.lista_selecionar()
            self.window_register.update()

        self.window_register.mainloop()

    def salvar_conteudo(self):
        if self.metodo == 'registro':
            self.code = self.init.brain.gerar_cod(self.init.brain)
        elif self.metodo == 'editor':
            self.code = self.roupa['cod'][0]

        if self.checar_vazio() and self.checar_venda():
            self.piece = {"cod": self.code,
                          "desc": self.descrição_geral_entrada.get().title(),
                          "categoria": self.categoria_lista.get(self.categoria_lista.curselection()).title(),
                          "tamanho": self.init.brain.registrar_item(self.init.brain, self.tamanhos_lista.curselection(), 'tamanho'),
                          "genero": self.genero_lista.get(self.genero_lista.curselection()).title(),
                          "marca": self.init.brain.preencher_vazio(self.marca_entrada.get()),
                          "cor": self.init.brain.registrar_item(self.init.brain, self.cores_lista.curselection(), 'cor'),
                          "valor_compra": self.valor_compra_entrada.get(),
                          "valor_venda": self.valor_venda_entrada.get(),
                          "data_entrada": self.init.brain.pegar_dia(),
                          "cod_venda": 0
                          }
            if self.metodo == 'registro':
                self.init.brain.salvar_roupa(self.piece)
                continuar = self.init.brain.continuar_cadastro(
                    self.window_register, self.code)
                if continuar:
                    self.descrição_geral_entrada.delete(0, END)
                    self.marca_entrada.delete(0, END)
                    self.tamanhos_lista.selection_clear(0, END)
                    self.valor_compra_entrada.delete(0, END)
                    self.valor_venda_entrada.delete(0, END)
                    self.radio_genero0.select()
                    self.cores_lista.selection_clear(0, END)
                    self.categoria_lista.selection_clear(0, END)
                    self.window_register.update()
                else:
                    self.window_register.destroy()
            elif self.metodo == 'editor':
                confirmar = self.init.brain.confirmar_editar(
                    self.window_register)
                if confirmar:
                    self.init.brain.editar_roupa(self.piece)
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
        elif len(self.valor_compra_entrada.get()) == 0:
            self.categoria_vazia = "Valor de Compra"
        elif len(self.valor_venda_entrada.get()) == 0:
            self.categoria_vazia = "Valor de Venda"

        if self.categoria_vazia == "":
            return True
        else:
            self.init.brain.categoria_em_branco(
                self.window_register, self.categoria_vazia)
            return False

    def checar_venda(self):
        if int(self.valor_venda_entrada.get()) <= int(self.valor_compra_entrada.get()) or int(self.valor_venda_entrada.get()) == 0:
            self.init.brain.venda_invalido(
                self.window_register, self.categoria_vazia)
            return False
        else:
            return True

    def checkbutton_see(self):
        if self.checked_state.get() == 0:
            self.valor_compra_entrada.config(show=" ")
        elif self.checked_state.get() == 1:
            self.valor_compra_entrada.config(show="")
        self.window_register.update()

    def lista_selecionar(self):
        self.func_lista(self.tamanhos_lista, 'tamanho')
        self.func_lista(self.cores_lista, 'cor')
        self.func_lista(self.genero_lista, 'genero')
        self.func_lista(self.categoria_lista, 'categoria')
        self.window_register.update()

    def func_lista(self, lista, word):
        index = self.init.brain.lista_select(self.init.brain,
                                             word, self.roupa[word][0])
        for i in index:
            lista.select_set(i)
        lista.see(index[0])

    def iniciar_venda(self):
        pass
