import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog


class Node:
    def __init__(self, valor):  # Método construtor da classe "Nó"
        self.info = valor
        self.prox = None

    def __str__(self):
        return str(self.info)


class Pilha:
    def __init__(self):  # Método construtor da classe "Pilha"
        self.ini = None
        self.n = 0  # Variável contadora

    def isEmpty(self):  # Retornar se estiver vazia
        return self.ini is None

    def size(self):  # Retorna o tamanho
        return self.n

    def InserirInicio(self, nome):
        novo = Node(nome)  # Cria um novo nó
        novo.prox = self.ini
        self.ini = novo
        self.n += 1

    # Remover determinado valor
    def pop(self, valor):
        if not self.ini:
            return
        if self.ini.info.upper() == valor.upper():
            self.ini = self.ini.prox
            self.n -= 1
            return
        atual = self.ini
        while atual.prox:
            if atual.prox.info.upper() == valor:
                atual.prox = atual.prox.info
                self.n -= 1
                return
            atual = atual.prox

    def __str__(self):
        no = self.ini
        msg = ""
        while no:
            msg += no.info + ", "
            no = no.prox
        return msg

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

    def estaRepetido(self, valor):
        atual = self.ini
        while atual is not None:
            if (valor.upper() == atual.info.upper()):
                return 1
            else:
                atual = atual.prox
        return 0

    # Função que adiciona um nome se verificar que este não está repetido
    def tentaInserir(self, op):
        nome = simpledialog.askstring("Entrada", "Digite um nome")
        if p.estaRepetido(nome):
            messagebox.showinfo("Erro", "Esse nome já está na lista. Tente outro.", icon=messagebox.ERROR)
        elif not nome.strip:
            messagebox.showinfo("Erro", "Nome em branco. Insira um nome válido.", icon=messagebox.ERROR)
        else:
            if op == 1:
                p.InserirInicio(nome)
            else:
                p.inserirNoFim(nome)
            messagebox.showinfo("Sucesso", "Adicionado com sucesso")

    def buscaNome(self):
        nome = simpledialog.askstring("Entrada", "Digite um nome")
        if p.estaRepetido(nome):
            messagebox.showinfo("Resultado", "Esse nome está na lista.", icon=messagebox.INFO)
        else:
            messagebox.showinfo("Resultado", "Esse nome não está na lista.", icon=messagebox.INFO)

    def removeNome(self):
        nome = simpledialog.askstring("Remoção", "Digite o nome para remover")
        if not p.estaRepetido(nome):
            messagebox.showinfo("Erro", "Esse nome não foi adicionado à lista. Tente novamente.", icon=messagebox.ERROR)
        else:
            p.pop(nome.upper())
            messagebox.showinfo("Sucesso", f'O nome "{nome}" foi removido com sucesso')

# Menu com as opcoes para inserir, remover e mostrar os elementos da Pilha
if __name__ == '__main__':
    p = Pilha()
    menu = "1. Inserir no Começo\n2. Inserir no fim\n3. Buscar nome\n4. Remover\n5. Tamanho\n6. Listar\n7. Sair\n"
    op = -1

    while (op != 7):
        op = simpledialog.askinteger("Entrada de valor", menu)
        if op == 1:
            p.tentaInserir(1)
        elif op == 2:
            p.tentaInserir(2)
        elif op == 3:
            p.buscaNome()
        elif op == 4:
            p.removeNome()
        elif op == 5:
            messagebox.showinfo("Tamanho", str(p.size()))
        elif op == 6:
            messagebox.showinfo("Elementos da Pilha", str(p))

    messagebox.showinfo("End of program", "Progama Encerrado!"),
