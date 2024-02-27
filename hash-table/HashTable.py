class Node:
    def __init__(self, valor):
        self.valor = valor
        self.prox = None

class HashTable:
    def __init__(self, M):
        self.M = M
        self.tab = [None] * M

    def hash(self, nome, funcao_hash):
        if funcao_hash == 1:
            return (ord(nome[0]) - ord('A')) % self.M
    
        else:   
            hash_value = 0
            for char in nome:
                hash_value += ord(char) 
            
            return hash_value % self.M       
        
    def inserir(self, nome, funcao_hash):
        i = self.hash(nome, funcao_hash)
        new_node = Node(nome)

        if self.tab[i] is None:
            self.tab[i] = new_node
        else:
            aux = self.tab[i]
            while aux.prox is not None:
                aux = aux.prox
            aux.prox = new_node  

    def listar(self):
        out = ""
        for i in range(self.M):
            out += f"Índice {i}: "
            aux = self.tab[i]
            while aux:
                out += f"{aux.valor} -> "
                aux = aux.prox
            out += "None\n\n"
        return out

    def numero_colisoes(self, funcao_hash):
        out = ""
        for i in range(self.M):
            cont = 0
            aux = self.tab[i]
            while aux:
                cont += 1
                aux = aux.prox
            if(self.M == 26 and funcao_hash == 1): #exibir letras
                out += f'{chr(ord("A") + i)}: {cont}\n'
            else: #exibir número do índice
                out += f'Índice {i}: {cont}\n'
        return out

