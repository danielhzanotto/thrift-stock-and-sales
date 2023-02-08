from tkinter import *
from brain import Brain, BrainVendas
from pesquisa import Pesquisa


class Venda:
    def __init__(self, produto=""):
        self.pesquisa = Pesquisa
        self.brain = Brain
        self.brain_vendas = BrainVendas
        self.colors = self.brain.get_data_dict()['cores_programa']

        self.codigo = self.brain_vendas.gerar_cod_venda(self.brain_vendas)
        self.produtos_venda_final = []
        self.valor_venda_final = []
        self.valor_desconto = 0
        self.valor_entrega = 0
        self.dia = self.brain.pegar_dia()

        self.window_venda = Toplevel()
        self.window_venda.title("Iniciar Venda")
        self.window_venda.config(padx=20, pady=20, bg=self.colors[0])

        self.mensagem_inicio = Label(self.window_venda, text=f"Venda {self.codigo}", font=(
            'Verdana', 16, "bold"), bg=self.colors[0], fg=self.colors[3])
        self.mensagem_inicio.grid(row=0, column=0, columnspan=6)

        self.divisor = Label(self.window_venda, text=" ", font=(
            'Verdana', 16, "bold"), bg=self.colors[0], fg=self.colors[3])
        self.divisor.grid(row=1, column=0, columnspan=6)

        self.nome_label = Label(self.window_venda, text="Nome:", font=(
            'Verdana', 9, "bold"), bg=self.colors[0], fg=self.colors[3])
        self.nome_label.grid(row=2, column=0)
        self.nome_entrada = Entry(
            self.window_venda, fg=self.colors[4], width=40)
        self.nome_entrada.grid(row=2, column=1, columnspan=3)

        self.cpf_label = Label(self.window_venda, text="CPF:", font=(
            'Verdana', 9, "bold"), bg=self.colors[0], fg=self.colors[3])
        self.cpf_label.grid(row=3, column=0)
        self.cpf_entrada = Entry(
            self.window_venda, fg=self.colors[4], width=40)
        self.cpf_entrada.grid(row=3, column=1, columnspan=3)

        self.cidade_label = Label(self.window_venda, text="Cidade:", font=(
            'Verdana', 9, "bold"), bg=self.colors[0], fg=self.colors[3])
        self.cidade_label.grid(row=4, column=0)
        self.cidade_entrada = Entry(
            self.window_venda, fg=self.colors[4], width=40)
        self.cidade_entrada.grid(row=4, column=1, columnspan=3)

        self.estado_label = Label(self.window_venda, text="UF:", font=(
            'Verdana', 9, "bold"), bg=self.colors[0], fg=self.colors[3])
        self.estado_label.grid(row=4, column=4)
        self.estado_entrada = Entry(
            self.window_venda, fg=self.colors[4], width=5)
        self.estado_entrada.grid(row=4, column=5)

        self.divisor = Label(self.window_venda, text="__________________________\n", font=(
            'Verdana', 16, "bold"), bg=self.colors[0], fg=self.colors[3])
        self.divisor.grid(row=5, column=0, columnspan=6)

        self.adicionar_label = Label(self.window_venda, text="Código do Produto:", font=(
            'Verdana', 9, "bold"), bg=self.colors[0], fg=self.colors[3])
        self.adicionar_label.grid(row=6, column=0, columnspan=2)
        self.adicionar_entrada = Entry(
            self.window_venda, fg=self.colors[4], width=28)
        self.adicionar_entrada.grid(row=6, column=2, columnspan=2)

        self.adicionar_button = Button(self.window_venda, text="Adicionar", bg=self.colors[1], fg=self.colors[4], highlightthickness=0, font=(
            'Verdana', 10), command=self.adicionar_produto_venda, width=11)
        self.adicionar_button.grid(row=6, column=4, columnspan=2)

        produto_var = Variable(value=[])
        self.produto_lista = Listbox(
            master=self.window_venda, height=8, width=60, listvariable=produto_var, fg=self.colors[4], font=('Courier', 8))
        self.produto_lista.grid(row=7, column=0, columnspan=6)

        self.pesquisar_button = Button(self.window_venda, text="Pesquisar Produtos", bg=self.colors[1], fg=self.colors[4], highlightthickness=0, font=(
            'Verdana', 10), command=self.pesquisar_produtos, width=24)
        self.pesquisar_button.grid(row=8, column=0, columnspan=3)

        self.remover_button = Button(self.window_venda, text="Remover", bg=self.colors[1], fg=self.colors[4], highlightthickness=0, font=(
            'Verdana', 10), command=self.remover_produto_venda, width=24)
        self.remover_button.grid(row=8, column=3, columnspan=3)

        self.divisor = Label(self.window_venda, text="__________________________\n", font=(
            'Verdana', 16, "bold"), bg=self.colors[0], fg=self.colors[3])
        self.divisor.grid(row=9, column=0, columnspan=6)

        self.pagamento_label = Label(self.window_venda, text="Pag.:", font=(
            'Verdana', 9, "bold"), bg=self.colors[0], fg=self.colors[3])
        self.pagamento_label.grid(row=10, column=0)
        self.pagamento_state = IntVar()
        self.pagamento_radio1 = Radiobutton(self.window_venda, text="Dinheiro", value=1, bg=self.colors[0], fg=self.colors[3],
                                            variable=self.pagamento_state, command=self.pagamento_used)
        self.pagamento_radio2 = Radiobutton(self.window_venda, text="Crédito ", value=2, bg=self.colors[0], fg=self.colors[3],
                                            variable=self.pagamento_state, command=self.pagamento_used)
        self.pagamento_radio3 = Radiobutton(self.window_venda, text="Débito      ", value=3, bg=self.colors[0], fg=self.colors[3],
                                            variable=self.pagamento_state, command=self.pagamento_used)
        self.pagamento_radio4 = Radiobutton(self.window_venda, text="Boleto", value=4, bg=self.colors[0], fg=self.colors[3],
                                            variable=self.pagamento_state, command=self.pagamento_used)
        self.pagamento_radio5 = Radiobutton(self.window_venda, text="Pix", value=5, bg=self.colors[0], fg=self.colors[3],
                                            variable=self.pagamento_state, command=self.pagamento_used)
        self.pagamento_radio1.grid(row=10, column=1)
        self.pagamento_radio2.grid(row=10, column=2)
        self.pagamento_radio3.grid(row=10, column=3)
        self.pagamento_radio4.grid(row=10, column=4)
        self.pagamento_radio5.grid(row=10, column=5)

        self.desconto_label = Label(self.window_venda, text="Desc.:", font=(
            'Verdana', 9, "bold"), bg=self.colors[0], fg=self.colors[3])
        self.desconto_label.grid(row=11, column=0)
        self.desconto_state = IntVar()
        self.desconto_radio1 = Radiobutton(self.window_venda, text="Nenhum", value=0, bg=self.colors[0], fg=self.colors[3],
                                           variable=self.desconto_state, command=self.desconto_used)
        self.desconto_radio2 = Radiobutton(self.window_venda, text="-------%", value=1, bg=self.colors[0], fg=self.colors[3],
                                           variable=self.desconto_state, command=self.desconto_used)
        self.desconto_radio3 = Radiobutton(self.window_venda, text="----R$", value=2, bg=self.colors[0], fg=self.colors[3],
                                           variable=self.desconto_state, command=self.desconto_used)
        self.desconto_radio1.grid(row=11, column=1)
        self.desconto_radio2.grid(row=11, column=2)
        self.desconto_radio3.grid(row=11, column=4)
        self.desconto_perc_entrada = Entry(
            self.window_venda, fg=self.colors[4], width=14, state='disabled')
        self.desconto_perc_entrada.bind('<KeyRelease>', self.fill_value)
        self.desconto_perc_entrada.grid(row=11, column=3)
        self.desconto_entrada = Entry(
            self.window_venda, fg=self.colors[4], width=5, state='disabled')
        self.desconto_entrada.bind('<KeyRelease>', self.fill_value)
        self.desconto_entrada.grid(row=11, column=5)

        self.entrega_label = Label(self.window_venda, text="Entrega:", font=(
            'Verdana', 9, "bold"), bg=self.colors[0], fg=self.colors[3])
        self.entrega_label.grid(row=12, column=0)
        self.entrega_state = IntVar()
        self.entrega_radio1 = Radiobutton(self.window_venda, text="Retirada ", value=0, bg=self.colors[0], fg=self.colors[3],
                                          variable=self.entrega_state, command=self.entrega_used)
        self.entrega_radio2 = Radiobutton(self.window_venda, text="Correios", value=1, bg=self.colors[0], fg=self.colors[3],
                                          variable=self.entrega_state, command=self.entrega_used)
        self.entrega_radio3 = Radiobutton(self.window_venda, text="Entrega Local", value=2, bg=self.colors[0], fg=self.colors[3],
                                          variable=self.entrega_state, command=self.entrega_used)
        self.entrega_radio4 = Radiobutton(self.window_venda, text="Outro", value=3, bg=self.colors[0], fg=self.colors[3],
                                          variable=self.entrega_state, command=self.entrega_used)
        self.entrega_radio1.grid(row=12, column=1)
        self.entrega_radio2.grid(row=12, column=2)
        self.entrega_radio3.grid(row=12, column=3)
        self.entrega_radio4.grid(row=12, column=4)
        self.entrega_entrada = Entry(
            self.window_venda, fg=self.colors[4], width=5)
        self.entrega_entrada.bind('<KeyRelease>', self.fill_value)
        self.entrega_entrada_fixo = Label(
            self.window_venda, text="0.00", font=(
                'Verdana', 9, "bold"), bg=self.colors[0], fg=self.colors[3])
        self.entrega_entrada_fixo.grid(row=12, column=5)

        self.valor_total_label = Label(self.window_venda, text="Total:", font=(
            'Verdana', 9, "bold"), bg=self.colors[0], fg=self.colors[3])
        self.valor_total_label.grid(row=14, column=0)

        self.valor_compra_label = Label(self.window_venda, text=f"R${float(sum(self.valor_venda_final)):.2f}", font=(
            'Verdana', 9), bg=self.colors[0], fg=self.colors[3])
        self.valor_compra_label.grid(row=14, column=1)

        self.valor_desconto_label = Label(self.window_venda, text=f"- R${self.valor_desconto:.2f}", font=(
            'Verdana', 9), bg=self.colors[0], fg=self.colors[3])
        self.valor_desconto_label.grid(row=14, column=2)

        self.valor_entrega_label = Label(self.window_venda, text=f"+ R${self.valor_entrega:.2f}", font=(
            'Verdana', 9), bg=self.colors[0], fg=self.colors[3])
        self.valor_entrega_label.grid(row=14, column=3)

        self.total_label = Label(self.window_venda, text=self.gerar_valor_total(), font=(
            'Verdana', 12, "bold"), bg=self.colors[0], fg=self.colors[3])
        self.total_label.grid(row=14, column=4, columnspan=2)

        self.divisor = Label(self.window_venda, text="__________________________\n", font=(
            'Verdana', 16, "bold"), bg=self.colors[0], fg=self.colors[3])
        self.divisor.grid(row=15, column=0, columnspan=6)

        self.cancelar_button = Button(
            self.window_venda, text="Cancelar", bg=self.colors[1], fg=self.colors[4], highlightthickness=0, font=('Verdana', 10), command=self.cancelar, width=15)
        self.cancelar_button.grid(row=16, column=0, columnspan=2)

        self.registrar_button = Button(
            self.window_venda, text="Registrar Venda", bg=self.colors[1], fg=self.colors[4], highlightthickness=0, font=('Verdana', 10), command=self.registrar_venda, width=33)
        self.registrar_button.grid(row=16, column=2, columnspan=4)

        if len(str(produto)) != 0:
            self.adicionar_produto_pesquisa(produto)
            self.window_venda.update()

        self.window_venda.mainloop()

    def cancelar(self):
        self.cancel = self.brain.confirmar_cancelar(self.window_venda)
        if self.cancel:
            self.window_venda.destroy()

    def adicionar_produto_venda(self):
        self.adicionar_produto_pesquisa(self.adicionar_entrada.get())

    def pesquisar_produtos(self):
        self.pesquisa(self, 'venda')

    def adicionar_produto_pesquisa(self, codigo):
        produto_info = self.brain_vendas.pegar_produto_venda_code(
            codigo)
        if produto_info[0] not in self.produtos_venda_final:
            self.produtos_venda_final.append(produto_info[0])
            self.produto_lista.insert(END, produto_info[1])
            self.valor_venda_final.append(produto_info[2])
            self.fill_value()

    def remover_produto_venda(self):
        self.produto_lista.delete(self.produto_lista.curselection()[0])

    def entrega_used(self):
        if self.entrega_state.get() == 0:
            self.entrega_entrada.grid_forget()
            self.entrega_entrada.delete(0, END)
            self.entrega_entrada_fixo.grid(row=12, column=5)
            self.entrega_entrada_fixo.config(text="0.00")
        elif self.entrega_state.get() == 2:
            self.entrega_entrada.grid_forget()
            self.entrega_entrada.delete(0, END)
            self.entrega_entrada_fixo.grid(row=12, column=5)
            self.entrega_entrada_fixo.config(text="5.00")
        elif self.entrega_state.get() == 1 or self.entrega_state.get() == 3:
            self.entrega_entrada_fixo.grid_forget()
            self.entrega_entrada.delete(0, END)
            self.entrega_entrada_fixo.config(text="0.00")
            self.entrega_entrada.grid(row=12, column=5)

        self.fill_value()

    def pagamento_used(self):
        self.pagamento = self.pagamento_state.get()

    def gerar_valor_total(self):
        self.valor_final = sum(self.valor_venda_final)

        if len(self.desconto_entrada.get()) != 0:
            self.valor_desconto = float(self.desconto_entrada.get())
        elif len(self.desconto_perc_entrada.get()) != 0:
            self.valor_desconto = self.valor_final * \
                (float(self.desconto_perc_entrada.get())/100)

        if len(self.entrega_entrada.get()) != 0:
            self.valor_entrega = float(self.entrega_entrada.get())
        elif int(self.entrega_entrada_fixo['text'][0]) != 0:
            self.valor_entrega = float(self.entrega_entrada_fixo['text'][0])

        self.valor_final -= self.valor_desconto
        self.valor_final += self.valor_entrega

        return f"R$ {float(self.valor_final): .2f}"

    def fill_value(self, binder=1):
        self.total_label.config(
            text=self.gerar_valor_total())
        self.valor_compra_label.config(
            text=f"R${float(sum(self.valor_venda_final)):.2f}")
        self.valor_desconto_label.config(text=f"- R${self.valor_desconto:.2f}")
        self.valor_entrega_label.config(text=f"+ R${self.valor_entrega:.2f}")
        self.window_venda.update()

    def desconto_used(self):
        if self.desconto_state.get() == 1:
            self.desconto_perc_entrada.config(state='normal')
            self.desconto_entrada.delete(0, END)
            self.desconto_entrada.config(state='disabled')
        elif self.desconto_state.get() == 2:
            self.desconto_entrada.config(state='normal')
            self.desconto_perc_entrada.delete(0, END)
            self.desconto_perc_entrada.config(state='disabled')
        elif self.desconto_state.get() == 0:
            self.desconto_perc_entrada.delete(0, END)
            self.desconto_entrada.delete(0, END)
            self.desconto_entrada.config(state='disabled')
            self.desconto_perc_entrada.config(state='disabled')

        self.fill_value()

    def registrar_venda(self):
        print(self.codigo)
        print(self.nome_entrada.get().title())
        print(self.cpf_entrada.get())  # tem que ter formato de cpf
        print(self.cidade_entrada.get().title())
        if len(self.estado_entrada.get()) != 2 and self.estado_entrada.get().isalpha():
            self.brain.valor_invalido(self.window_venda, 'UF')
            pass
        else:
            print(self.estado_entrada.get().upper())
        print(self.produtos_venda_final)
        print(self.valor_final)
        print(self.valor_entrega)
        print(self.brain_vendas.pegar_nomes_metodos('tipo_entrega',
              self.entrega_state.get()))
        print(self.valor_desconto)
        if self.pagamento_state.get() == 0:
            self.brain.categoria_em_branco(self.window_venda, 'PAGAMENTO')
        else:
            print(self.brain_vendas.pegar_nomes_metodos('tipo_pagamento',
                                                        self.pagamento_state.get() - 1))
            print(self.pagamento_state.get())
        print(self.dia)
