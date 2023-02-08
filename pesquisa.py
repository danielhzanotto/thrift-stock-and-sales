from tkinter import *

from lista_pesquisa import ListaPesquisa


class Pesquisa:
    def __init__(self, init, metodo):
        self.lista_pesquisa = ListaPesquisa
        self.init = init
        self.colors = self.init.brain.get_data_dict()['cores_programa']
        self.metodo = metodo

        self.window_pesquisa = Toplevel()
        self.window_pesquisa.title("Pesquisa")
        self.window_pesquisa.config(padx=20, pady=20, bg=self.colors[0])

        self.mensagem_pesquisa = Label(self.window_pesquisa, text="Insira os dados da pesquisa", font=(
            'Verdana', 16, "bold"), bg=self.colors[0], fg=self.colors[3])
        self.mensagem_pesquisa.grid(row=0, column=0, columnspan=6)

        self.radio_base = IntVar()
        self.radio_code = Radiobutton(self.window_pesquisa, text="Pesquisar por Código", font=(
            'Verdana', 12), value=1, bg=self.colors[0], fg=self.colors[3], variable=self.radio_base, command=self.radio_used)
        self.radio_code.grid(row=1, column=0, columnspan=3)
        self.radio_categoria = Radiobutton(self.window_pesquisa, text="Pesquisar por Categoria", value=2, font=(
            'Verdana', 12), bg=self.colors[0], fg=self.colors[3], variable=self.radio_base, command=self.radio_used)
        self.radio_categoria.grid(row=1, column=3, columnspan=3)

        self.divisor = Label(self.window_pesquisa, text="________________________________\n", font=(
            'Verdana', 16, "bold"), bg=self.colors[0], fg=self.colors[3])
        self.divisor.grid(row=2, column=0, columnspan=6)

        # pesquisar por código
        self.codigo_label = Label(self.window_pesquisa, text="Digite Código da peça:", font=(
            'Verdana', 9, 'bold'), bg=self.colors[0], fg=self.colors[3])
        self.codigo_entrada = Entry(self.window_pesquisa, width=47)
        self.vazio_codigo_label = Label(self.window_pesquisa, text="\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n", font=(
            'Verdana', 6), bg=self.colors[0], fg=self.colors[3])

        # pesquisar por categoria
        # // pesquisar por vendidos
        self.radio_venda = IntVar()
        self.radio_ambos = Radiobutton(self.window_pesquisa, text="Pesquisar Todas", font=(
            'Verdana', 9, 'bold'), value=0, bg=self.colors[0], fg=self.colors[3], variable=self.radio_venda)
        self.radio_estoque = Radiobutton(self.window_pesquisa, text="Pesquisar Estoque", font=(
            'Verdana', 9, 'bold'), value=1, bg=self.colors[0], fg=self.colors[3], variable=self.radio_venda)
        self.radio_vendido = Radiobutton(self.window_pesquisa, text="Pesquisar Vendidas", font=(
            'Verdana', 9, 'bold'), value=2, bg=self.colors[0], fg=self.colors[3], variable=self.radio_venda)
        self.vazio_label = Label(self.window_pesquisa, text="\n", font=(
            'Verdana', 6), bg=self.colors[0], fg=self.colors[3])
        # // pesquisar por descrição
        self.desc_label = Label(self.window_pesquisa, text="Pesquisar Descrição:", font=(
            'Verdana', 9, 'bold'), bg=self.colors[0], fg=self.colors[3])
        self.desc_entrada = Entry(self.window_pesquisa, width=47)
        # // pesquisar por marca
        self.marca_label = Label(self.window_pesquisa, text="Pesquisar Marca:", font=(
            'Verdana', 9, 'bold'), bg=self.colors[0], fg=self.colors[3])
        self.marca_entrada = Entry(self.window_pesquisa, width=47)
        # // pesquisar por categoria
        self.categoria_label = Label(self.window_pesquisa, text="Pesquisar Categoria:", font=(
            'Verdana', 9, 'bold'), bg=self.colors[0], fg=self.colors[3])
        categorias_var = Variable(
            value=self.init.brain.get_data_dict()['categoria'])
        self.categoria_lista = Listbox(
            master=self.window_pesquisa, height=11, width=20, listvariable=categorias_var, fg=self.colors[4], selectmode=MULTIPLE, exportselection=0)
        # // pesquisar por cor
        self.cores_label = Label(self.window_pesquisa, text="Pesquisar Cor:", font=(
            'Verdana', 9, 'bold'), bg=self.colors[0], fg=self.colors[3])
        cores_var = Variable(value=self.init.brain.get_data_dict()['cor'])
        self.cores_lista = Listbox(
            master=self.window_pesquisa, height=11, width=15, listvariable=cores_var, selectmode=MULTIPLE, fg=self.colors[4], exportselection=0)
        # // pesquisar por genero
        self.genero_label = Label(self.window_pesquisa, text="Pesquisar Gênero:", font=(
            'Verdana', 9, 'bold'), bg=self.colors[0], fg=self.colors[3])
        genero_var = Variable(
            value=self.init.brain.get_data_dict()['genero'])
        self.genero_lista = Listbox(
            master=self.window_pesquisa, height=3, width=20, listvariable=genero_var, selectmode=MULTIPLE, fg=self.colors[4], exportselection=0)
        # // pesquisar por tamanho
        self.tamanho_label = Label(self.window_pesquisa, text="Pesquisar Tamanho:", font=(
            'Verdana', 9, 'bold'), bg=self.colors[0], fg=self.colors[3])
        tamanho_var = Variable(
            value=self.init.brain.get_data_dict()['tamanho'])
        self.tamanho_lista = Listbox(
            master=self.window_pesquisa, height=6, width=20, listvariable=tamanho_var, fg=self.colors[4], selectmode=MULTIPLE, exportselection=0)

        # botao de pesquisar
        self.divisor2 = Label(self.window_pesquisa, text="________________________________\n", font=(
            'Verdana', 16, "bold"), bg=self.colors[0], fg=self.colors[3])
        self.divisor2.grid(row=12, column=0, columnspan=6)

        self.cancelar_button = Button(
            self.window_pesquisa, text="Cancelar", width=15, bg=self.colors[1], fg=self.colors[4], highlightthickness=0, font=('Verdana', 10), command=self.cancelar)
        self.cancelar_button.grid(row=13, column=0)

        self.pesquisar_button = Button(self.window_pesquisa, text="Pesquisar", font=(
            'Verdana', 10), bg=self.colors[1], fg=self.colors[4], width=42, highlightthickness=0, command=self.pesquisar)

        self.window_pesquisa.mainloop()

    def radio_used(self):
        if self.radio_base.get() == 1:
            self.radio_estoque.grid_forget()
            self.radio_vendido.grid_forget()
            self.radio_ambos.grid_forget()
            self.vazio_label.grid_forget()
            self.desc_label.grid_forget()
            self.desc_entrada.grid_forget()
            self.marca_label.grid_forget()
            self.marca_entrada.grid_forget()
            self.categoria_label.grid_forget()
            self.categoria_lista.grid_forget()
            self.cores_label.grid_forget()
            self.cores_lista.grid_forget()
            self.genero_label.grid_forget()
            self.genero_lista.grid_forget()
            self.tamanho_label.grid_forget()
            self.tamanho_lista.grid_forget()

            self.codigo_label.grid(row=3, column=0, columnspan=2)
            self.codigo_entrada.grid(row=3, column=2, columnspan=4)
            self.vazio_codigo_label.grid(row=4, column=0, columnspan=6)
            self.pesquisar_button.grid(row=13, column=1, columnspan=5)
            self.window_pesquisa.update()

        elif self.radio_base.get() == 2:
            self.codigo_label.grid_forget()
            self.codigo_entrada.grid_forget()
            self.vazio_codigo_label.grid_forget()

            self.radio_ambos.grid(row=3, column=0, columnspan=2)
            self.radio_estoque.grid(row=3, column=2, columnspan=2)
            self.radio_vendido.grid(row=3, column=4, columnspan=2)
            self.vazio_label.grid(row=4, column=0, columnspan=6)
            self.desc_label.grid(row=5, column=0, columnspan=2)
            self.desc_entrada.grid(row=5, column=2, columnspan=4)
            self.marca_label.grid(row=6, column=0, columnspan=2)
            self.marca_entrada.grid(row=6, column=2, columnspan=4)
            self.categoria_label.grid(row=7, column=0, columnspan=2)
            self.categoria_lista.grid(row=8, column=0, columnspan=2, rowspan=4)
            self.cores_label.grid(row=7, column=2, columnspan=2)
            self.cores_lista.grid(row=8, column=2, columnspan=2, rowspan=4)
            self.genero_label.grid(row=7, column=4, columnspan=2)
            self.genero_lista.grid(row=8, column=4, columnspan=2)
            self.tamanho_label.grid(row=9, column=4, columnspan=2)
            self.tamanho_lista.grid(row=10, column=4, columnspan=2)
            self.pesquisar_button.grid(row=13, column=1, columnspan=5)
            self.window_pesquisa.update()

    def cancelar(self):
        self.window_pesquisa.destroy()

    def pesquisar(self):
        if self.radio_base.get() == 1:
            if len(self.codigo_entrada.get()) == 0:
                self.init.brain.categoria_em_branco(
                    self.window_pesquisa, 'código')
            else:
                self.df_pesquisa = self.init.brain.get_pesquisa_code(
                    self.codigo_entrada.get())
        elif self.radio_base.get() == 2:
            self.data_pesquisa = [self.radio_venda.get(), self.cores_lista.curselection(), self.categoria_lista.curselection(
            ), self.genero_lista.curselection(), self.tamanho_lista.curselection(), self.marca_entrada.get().title(), self.desc_entrada.get()]
            self.df_pesquisa = self.init.brain.get_pesquisa(
                self.init.brain, self.data_pesquisa)

        self.lista_pesquisa.criar_lista(
            self, self.df_pesquisa, self.window_pesquisa)
        self.window_pesquisa.update()
        if len(self.df_pesquisa) == 0:
            self.init.brain.pesquisa_vazia(self.window_pesquisa)

    def get_code(self):
        selection = self.resultado_lista.get(
            self.resultado_lista.curselection())
        return int(selection.split(" ")[0][1:-1])

    def editar_roupa(self):
        selection_code = self.get_code()
        df_code = self.init.brain.get_pesquisa_code(selection_code)
        df_dict = self.init.brain.df_to_dict(df_code)
        self.window_pesquisa.destroy()
        self.init.reg(self.init, 'editor', df_dict)

    def adicionar_venda(self):
        selection_code = self.get_code()
        if self.metodo == 'pesquisa':
            self.window_pesquisa.destroy()
            self.init.venda(produto=selection_code)

        elif self.metodo == 'venda':
            self.window_pesquisa.destroy()
            self.init.adicionar_produto_pesquisa(selection_code)
