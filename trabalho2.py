import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog


class Node:
    def _init_(self, valor):  # Método construtor da classe "Nó"
        self.info = valor
        self.prox = None

    def _str_(self):
        return str(self.info)


class Pilha:
    def _init_(self):  # Método construtor da classe "Pilha"
        self.ini = None
        self.n = 0  # Variável contadora

    def isEmpty(self):  # Retornar se estiver vazia
        return self.ini is None

    def size(self):  # Retorna o tamanho
        return self.n

    # Insercao no inicio da lista
    def InserirInicio(self, val):
        novo = Node(val)  # Cria um novo nó
        novo.prox = self.ini
        self.ini = novo
        self.n += 1

    # Remocao do inicio da lista
    def pop(self, valor):
        if not self.ini:
            return
        if self.ini.info == valor:
            self.ini = self.ini.prox
            return
        atual = self.ini
        while atual.prox:
            if atual.prox.info == valor:
                atual.prox = atual.prox.info
                return
            atual = atual.prox

    def _str_(self):
        no = self.ini
        msg = ""
        while no:
            msg += no.info + ", "
            no = no.prox
        return msg

    # Inserir no fim da lista
    def inserirNoFim(self, valor):
        novo = Node(valor)

        if not self.ini:
            self.ini = novo
            self.n += 1
        else:
            atual = self.ini
            while atual.prox:
                atual = atual.prox
        atual.prox = novo
        self.n += 1


# Menu com as opcoes para inserir, remover e mostrar os elementos da Pilha
if __name__ == '__main__':
    p = Pilha()
    menu = "1.Inserir no Começo\n2.Inserir no fim\n3.Remover\n4.Tamanho\n5.Listar\n6.Sair"
    op = -1

    while (op != 6):
        op = simpledialog.askinteger("Entrada de valor", menu)
        if op == 1:
            val = simpledialog.askstring("Entrada", "Digite um valor")
            p.InserirInicio(val)
        elif op == 2:
            val = simpledialog.askstring("Entrada", "Digite um valor")
            p.inserirNoFim(val)
        elif op == 3:
            val = simpledialog.askstring(
                "Remoção", "Digite o valor para remover")
            p.pop(val)
            messagebox.showinfo("Nome removido", val)
        elif op == 4:
            messagebox.showinfo("Tamanho", str(p.size()))
        elif op == 5:
            messagebox.showinfo("Elementos da Pilha", str(p))
    messagebox.showinfo("End of program", "Progama Encerrado!"),
