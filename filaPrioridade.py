from tkinter import messagebox
from tkinter import simpledialog

class Node:
    def __init__(self, nome, idade, classe_prioridade):
        self.nome = nome
        self.idade = idade
        self.classe_prioridade = classe_prioridade
        self.proximo = None

class Atendimento:
    def __init__(self):
        self.fila_prioritaria = None
        self.fila_normal = None
        self.size_prioridade = 0
        self.size_normal = 0
        self.size_pendente = 0

    def adicionarCliente(self, nome, idade, prioridade=False, classe_prioridade=None):
        novo_cliente = Node(nome, idade, classe_prioridade)
        self.size_pendente += 1
        if prioridade:
            if not self.fila_prioritaria:
                novo_cliente.proximo = self.fila_prioritaria
                self.fila_prioritaria = novo_cliente    
            else:
                atual = self.fila_prioritaria
                anterior = None
                while atual and atual.classe_prioridade <= classe_prioridade:
                    anterior = atual
                    atual = atual.proximo
                if anterior:
                    anterior.proximo = novo_cliente
                    novo_cliente.proximo = atual
                else:
                    novo_cliente.proximo = self.fila_prioritaria
                    self.fila_prioritaria = novo_cliente
        else:
            if not self.fila_normal:
                self.fila_normal = novo_cliente
            else:
                atual = self.fila_normal
                while atual.proximo:
                    atual = atual.proximo
                atual.proximo = novo_cliente

    def atenderProximo(self):
        if self.fila_prioritaria:
            cliente = self.fila_prioritaria
            self.fila_prioritaria = cliente.proximo
            self.size_prioridade += 1
            self.size_pendente -= 1
            return messagebox.showinfo("Informação", f"Cliente atendido: {cliente.nome} (Idade: {cliente.idade})")
        
        elif self.fila_normal:
            cliente = self.fila_normal
            self.fila_normal = cliente.proximo
            self.size_normal += 1
            self.size_pendente -= 1
            return messagebox.showinfo("Informação",f"Cliente atendido: {cliente.nome} (Idade: {cliente.idade})")
        else:
            return messagebox.showinfo("Erro", "Fila de atendimento vazia.")
        
    def estatisticas(self):
        if self.size_prioridade == 0 and self.size_normal == 0:
            messagebox.showinfo("Estatísticas Parciais","Nenhum cliente foi atendido!")
        elif self.size_prioridade > 0 and self.size_normal == 0:    
            messagebox.showinfo("Estatísticas Parciais", f"Atendimento(s) prioritário(s): {self.size_prioridade}\nNenhum cliente da fila formal foi atendido.!\nTotal: {self.size_prioridade + self.size_normal} atendimento(s)")
        elif self.size_prioridade == 0  and self.size_normal > 0:
            messagebox.showinfo("Estatísticas Parciais", f"Ainda não foram antendidos clientes da fila prioritária.\nAtendimento(s) normal(is): {self.size_normal}.\nTotal: {self.size_prioridade + self.size_normal} atendimento(s) ")
        else:    
            messagebox.showinfo("Estatísticas Parciais",f"Atendimento(s) prioritário(s): {self.size_prioridade}.\nAtendimento(s) normal(is): {self.size_normal}.\nTotal: {self.size_prioridade + self.size_normal} atendimento(s)")

    def listarPessoas(self):
        atual = self.fila_prioritaria
        prioridade = ''
        while atual:
            prioridade += atual.nome + " (" + str(atual.idade) + " anos)" + "; "
            atual = atual.proximo  
        atual = self.fila_normal
        normal = ''
        while atual:
            normal += atual.nome + " (" + str(atual.idade) + " anos)" + "; "
            atual = atual.proximo    

        messagebox.showinfo(f"Pessoas na fila", f"Fila prioritária: {prioridade}\nFila normal: {normal}")

def obter_classe_prioridade():
    if idade >= 60:
        idoso = True
    else:
        idoso = False
        classe_prioridade = 5

    if idoso:
        if idade >= 100:
            classe_prioridade = 0
        elif idade >= 90:
            classe_prioridade = 1
        elif idade >= 80:
            classe_prioridade = 2
        elif idade >= 70:
            classe_prioridade = 3
        else:
            classe_prioridade = 4
    
    messagebox.showinfo("Classe de Prioridade",f'A classe de prioridade foi a {classe_prioridade}.')
    return classe_prioridade

if __name__ == '__main__':
    atendimento = Atendimento()

    while True:
        Menu = "1. Adicionar cliente prioritário\n2. Adicionar cliente normal\n3. Atender próximo cliente\n4. Estatísticas Parciais\n5. Listar\n6. Encerrar" 

        opcao = simpledialog.askstring("Menu Pricipal", "Escolha uma opção\n\n"+Menu)

        if opcao == '1':
            nome = simpledialog.askstring("Nome", "Digite o nome do cliente")
            idade = simpledialog.askinteger("Idade", "Digite a idade do cliente: ")
            classe_prioridade = obter_classe_prioridade()
            atendimento.adicionarCliente(nome, idade, prioridade=True, classe_prioridade = classe_prioridade)
        elif opcao == '2':
            nome = simpledialog.askstring("Nome", "Digite o nome do cliente")
            idade = simpledialog.askinteger("Idade", "Digite a idade do cliente: ")
            atendimento.adicionarCliente(nome, idade)
        elif opcao == '3':
            cliente_atendido = atendimento.atenderProximo()
        elif opcao == '4':
            atendimento.estatisticas()
        elif opcao == '5':
            if atendimento.size_pendente == 0:
                messagebox.showinfo("Erro", "As filas estão vazias!")
            else:    
                atendimento.listarPessoas()
        elif opcao == '6':
            if atendimento.size_pendente == 0:
                total = atendimento.size_prioridade + atendimento.size_normal
                if total == 0:
                    messagebox.showinfo("Estatísticas Finais","Ninguém foi atendido!")
                    break
                else:
                    estatisticas = f"Atendimento(s) prioritario(s): {atendimento.size_prioridade:.2f} ({(atendimento.size_prioridade/total*100):.2f}%)\nAtendimento(s) normal(is): {atendimento.size_normal:.2f} ({(atendimento.size_normal/total*100):.2f}%)"
                    messagebox.showinfo("Estatísticas Finais", estatisticas)
                    break
            else:
                messagebox.showinfo("Erro",f"Ainda resta(m) {atendimento.size_pendente} pessoa(s) para atendimento.")
        else:
            messagebox.showinfo("Erro","Opção inválida. Tente novamente.")