from tkinter import *

from registradora import Registradora
from brain import Brain
from pesquisa import Pesquisa
from venda import Venda
from pesquisa_venda import PesquisaVenda


class Inicial:
    def __init__(self):
        self.brain = Brain
        self.reg = Registradora
        self.venda = Venda
        self.colors = self.brain.get_categorias_dict()['cores_programa']
        self.dados = self.brain.get_dados_dict()

        self.window_main = Tk()
        self.window_main.title("Vibe Verde")
        self.window_main.config(
            padx=20, pady=20, bg=self.colors[0])

        self.main_label = Label(
            self.window_main, text=self.dados['nome_fantasia'][0], font=('Verdana', 20, "bold"), bg=self.colors[0], fg=self.colors[3])
        self.main_label.grid(row=0, column=0, columnspan=2)

        self.divisor = Label(self.window_main, text="___________________________\n", font=(
            'Verdana', 16, "bold"), bg=self.colors[0], fg=self.colors[3])
        self.divisor.grid(row=1, column=0, columnspan=2)

        self.registrar_button = Button(self.window_main, text="Registrar Peça", font=(
            'Verdana', 12), bg=self.colors[1], fg=self.colors[4], highlightthickness=0, command=self.registrar, width=20)
        self.registrar_button.grid(row=2, column=1)

        self.vender_button = Button(self.window_main, text="Iniciar Venda", font=(
            'Verdana', 12), bg=self.colors[1], fg=self.colors[4], highlightthickness=0, command=self.iniciar_venda, width=20)
        self.vender_button.grid(row=2, column=0)

        self.vazio_label = Label(self.window_main, text="\n", font=(
            'Verdana', 6), bg=self.colors[0], fg=self.colors[3])
        self.vazio_label.grid(row=3, column=0, columnspan=2)

        self.buscar_button = Button(self.window_main, text="Buscar Peça", font=(
            'Verdana', 12), bg=self.colors[1], fg=self.colors[4], highlightthickness=0, command=self.buscar_produto, width=20)
        self.buscar_button.grid(row=4, column=1)

        self.buscar_venda_button = Button(self.window_main, text="Buscar Venda", font=(
            'Verdana', 12), bg=self.colors[1], fg=self.colors[4], highlightthickness=0, command=self.buscar_venda, width=20)
        self.buscar_venda_button.grid(row=4, column=0)

        self.vazio_label = Label(self.window_main, text="\n", font=(
            'Verdana', 6), bg=self.colors[0], fg=self.colors[3])
        self.vazio_label.grid(row=5, column=0, columnspan=2)

        self.gerar_relatorio_button = Button(self.window_main, text="Gerar Relatórios", font=(
            'Verdana', 12), bg=self.colors[1], fg=self.colors[4], highlightthickness=0, command=self.gerar_relatorios, width=20)
        self.gerar_relatorio_button.grid(row=6, column=0)

        self.devolver_button = Button(self.window_main, text="Efetuar Devolução", font=(
            'Verdana', 12), bg=self.colors[1], fg=self.colors[4], highlightthickness=0, command=self.efetuar_devolução, width=20)
        self.devolver_button.grid(row=6, column=1)

        self.divisor = Label(self.window_main, text="___________________________\n", font=(
            'Verdana', 16, "bold"), bg=self.colors[0], fg=self.colors[3])
        self.divisor.grid(row=8, column=0, columnspan=2)

        self.configurar_button = Button(self.window_main, text="Configurações", font=(
            'Verdana', 8), bg=self.colors[1], fg=self.colors[4], highlightthickness=0, command=self.configurar)
        self.configurar_button.grid(row=9, column=1)

        self.mensagem = Label(self.window_main, text=self.dados['mensagem'][0], font=(
            'Verdana', 10), bg=self.colors[0], fg=self.colors[3])
        self.mensagem.grid(row=9, column=0)

        self.window_main.mainloop()

    def iniciar_venda(self):
        self.venda()

    def registrar(self):
        self.reg(self, 'registro')

    def buscar_produto(self):
        Pesquisa(self, 'pesquisa')

    def buscar_venda(self):
        self.brain.em_dev(self.window_main)

    def gerar_relatorios(self):
        self.brain.em_dev(self.window_main)

    def efetuar_devolução(self):
        self.brain.em_dev(self.window_main)

    def configurar(self):
        self.brain.em_dev(self.window_main)


Inicial()
