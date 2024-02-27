import time
from collections import deque, UserList

class MinhaUserList(UserList):
    def inserir(self, palavras):
        for palavra in palavras:
            self.append(palavra)

def inserir_em_lista(container, palavras):
    for palavra in palavras:
        container.append(palavra)

def inserir_em_deque(container, palavras):
    for palavra in palavras:
        container.append(palavra)

def ler_palavras(arquivo):
    with open(arquivo, 'r', encoding='utf-8') as f:
        return f.read().split()

arquivo = 'leipzig100k.txt'
palavras = ler_palavras(arquivo)

def calcular_tempo(container, operacao, palavras):
    inicio = time.time()
    operacao(container, palavras)
    fim = time.time()
    return (fim - inicio) * 1000  # Convertendo para milissegundos

# Lista Normal
lista_normal = []
tempo_lista_normal = calcular_tempo(lista_normal, inserir_em_lista, palavras)

# Deque
deque_container = deque()
tempo_deque = calcular_tempo(deque_container, inserir_em_deque, palavras)

# UserList
user_list = MinhaUserList()
tempo_user_list = calcular_tempo(user_list, MinhaUserList.inserir, palavras)

print("TEMPO DE INSERÇÃO".center(30))
print("Lista normal: {:>9.2f} ms".format(tempo_lista_normal))
print("Deque: {:>16.2f} ms".format(tempo_deque))
print("UserList: {:>13.2f} ms".format(tempo_user_list))
print("")

def pesquisar_palavra(palavra, lista):
    if palavra in lista:
        return True, lista.index(palavra)
    else:
        return False, -1

palavras_especificas = ["Lisbon", "NASA", "Kyunghee", "Konkuk", "Sogang", "momentarily", "rubella", "vaccinations", "government", "Authorities"]

def pesquisar_palavras_especificas(lista, palavras_especificas):
    tempos = []
    for palavra in palavras_especificas:
        inicio = time.time()
        encontrada, posicao = pesquisar_palavra(palavra, lista)
        fim = time.time()
        tempo = (fim - inicio) * 1000  # Convertendo para milissegundos
        tempos.append(tempo)
    return tempos

def calcular_tempo_medio(tempos):
    return sum(tempos) / len(tempos) if len(tempos) > 0 else 0

print("TEMPO MÉDIO DE BUSCA".center(30))
print("Estrutura / Tempo Médio (ms)")

# Calcular tempo médio de busca nas palavras específicas em cada estrutura de dados
tempos_lista_normal_busca = pesquisar_palavras_especificas(lista_normal, palavras_especificas)
tempo_medio_lista_normal_busca = calcular_tempo_medio(tempos_lista_normal_busca)
print("Lista normal: {:>10.2f}".format(tempo_medio_lista_normal_busca))

tempos_deque_busca = pesquisar_palavras_especificas(deque_container, palavras_especificas)
tempo_medio_deque_busca = calcular_tempo_medio(tempos_deque_busca)
print("Deque: {:>17.2f}".format(tempo_medio_deque_busca))

tempos_user_list_busca = pesquisar_palavras_especificas(user_list, palavras_especificas)
tempo_medio_user_list_busca = calcular_tempo_medio(tempos_user_list_busca)
print("UserList: {:>14.2f}".format(tempo_medio_user_list_busca))
print("")

def remover_palavras_especificas(lista, palavras):
    inicio = time.time()
    for palavra in palavras:
        if palavra in lista:
            lista.remove(palavra)
    fim = time.time()
    return (fim - inicio) * 1000  # Convertendo para milissegundos

print("TEMPO MÉDIO DE EXCLUSÃO".center(30))
print("Estrutura / Tempo Médio (ms)")

# Calcular tempo médio de exclusão das palavras específicas em cada estrutura de dados
tempo_medio_remocao_lista_normal = calcular_tempo_medio(pesquisar_palavras_especificas(lista_normal, palavras_especificas))
print("Lista normal: {:>10.2f}".format(tempo_medio_remocao_lista_normal))

tempo_medio_remocao_deque = calcular_tempo_medio(pesquisar_palavras_especificas(deque_container, palavras_especificas))
print("Deque: {:>17.2f}".format(tempo_medio_remocao_deque))

tempo_medio_remocao_user_list = calcular_tempo_medio(pesquisar_palavras_especificas(user_list, palavras_especificas))
print("UserList: {:>14.2f}".format(tempo_medio_remocao_user_list))
