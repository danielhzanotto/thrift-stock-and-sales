from tkinter import *

from registradora import Registradora
from brain import Brain
from pesquisa import Pesquisa
from venda import Venda

COLORS = ["#fefae0", "#dda15e", "#bc6c25", "#606c38", "#283618"]


class Inicial:
    def __init__(self):
        self.brain = Brain
        self.colors = self.brain.get_data(self)[2]

        self.window_main = Tk()
        self.window_main.title("Vibe Verde")
        self.window_main.config(
            padx=20, pady=20, bg=self.colors[0])

        self.main_label = Label(
            self.window_main, text="VIBE VERDE", font=('Verdana', 20, "bold"), bg=self.colors[0], fg=self.colors[3])
        self.main_label.grid(row=0, column=0, columnspan=3)

        self.registrar_button = Button(self.window_main, text="Registrar Peça", font=(
            'Verdana', 12), bg=self.colors[1], fg=self.colors[4], highlightthickness=0, command=self.registrar)
        self.registrar_button.grid(row=1, column=0)

        self.buscar_button = Button(self.window_main, text="Buscar Peça", font=(
            'Verdana', 12), bg=self.colors[1], fg=self.colors[4], highlightthickness=0, command=self.buscar)
        self.buscar_button.grid(row=1, column=1)

        self.vender_button = Button(self.window_main, text="Iniciar Venda", font=(
            'Verdana', 12), bg=self.colors[1], fg=self.colors[4], highlightthickness=0, command=self.iniciar_venda)
        self.vender_button.grid(row=1, column=2)

        self.window_main.mainloop()

    def registrar(self):
        Registradora(self)

    def buscar(self):
        Pesquisa(self)

    def iniciar_venda(self):
        Venda()


Inicial()
