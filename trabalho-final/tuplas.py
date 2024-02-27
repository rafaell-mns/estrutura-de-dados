import time
from collections import namedtuple

# Definição da namedtuple
Palavra = namedtuple("Palavra", ["palavra", "tamanho"])

def inserir_em_tupla_fixa(palavras):
    inicio = time.time()
    tupla_container = [None] * len(palavras)
    contador = 0
    for idx, palavra in enumerate(palavras):
        tupla_container[idx] = Palavra(palavra, len(palavra))
    fim = time.time()
    tempo = (fim - inicio) * 1000  # Convertendo para milissegundos
    return tuple(tupla_container), tempo


def inserir_em_namedtuple(palavras):
    inicio = time.time()
    namedtuple_container = []
    for idx, palavra in enumerate(palavras):
        namedtuple_container.append(Palavra(palavra, len(palavra)))

    fim = time.time()
    tempo = (fim - inicio) * 1000  # Convertendo para milissegundos
    return namedtuple_container, tempo

def ler_palavras(arquivo):
    with open(arquivo, 'r', encoding='utf-8') as f:
        return [word for line in f for word in line.split()]

arquivo = 'leipzig100k.txt'
palavras = ler_palavras(arquivo)

# Tupla
tupla_container_fixa, tempo_tupla_fixa = inserir_em_tupla_fixa(palavras)

# Namedtuple
namedtuple_container, tempo_namedtuple = inserir_em_namedtuple(palavras)

print("TEMPO DE INSERÇÃO".center(30))
print("Estrutura / Tempo (ms)")
print("Tupla: {:>14.2f} ms".format(tempo_tupla_fixa))
print("Namedtuple: {:>9.2f} ms".format(tempo_namedtuple))
print("")

def pesquisar_palavra(palavra, container):
    for idx, item in enumerate(container):
        if item.palavra == palavra:
            return True, idx
    return False, -1

palavras_especificas = ["Lisbon", "NASA", "Kyunghee", "Konkuk", "Sogang", "momentarily", "rubella", "vaccinations", "government", "Authorities"]

def pesquisar_palavras_especificas(container, palavras_especificas):
    tempos = []
    for palavra in palavras_especificas:
        inicio = time.time()
        encontrada, posicao = pesquisar_palavra(palavra, container)
        fim = time.time()
        tempo = (fim - inicio) * 1000  # Convertendo para milissegundos
        tempos.append((palavra, tempo, encontrada))
    return tempos

def calcular_tempo_medio(tempos):
    return sum(tempo for palavra, tempo, encontrada in tempos) / len(tempos) if len(tempos) > 0 else 0

print("TEMPO DE BUSCA".center(30))
print("Estrutura / Palavra / Encontrada? / Tempo (ms)")

# Calcular tempo de busca de cada palavra nas palavras específicas em cada estrutura de dados
tempos_tupla_fixa_busca = pesquisar_palavras_especificas(tupla_container_fixa, palavras_especificas)
for palavra, tempo, encontrada in tempos_tupla_fixa_busca:
    encontrado = "sim" if encontrada else "não"
    print("Tupla {:>12} {:<5} {:>8.2f}".format(palavra, encontrado, tempo))
print("Tupla - Tempo Médio: {:.2f} ms".format(calcular_tempo_medio(tempos_tupla_fixa_busca)))
print("")

tempos_namedtuple_busca = pesquisar_palavras_especificas(namedtuple_container, palavras_especificas)
for palavra, tempo, encontrada in tempos_namedtuple_busca:
    encontrado = "sim" if encontrada else "não"
    print("Namedtuple {:>8} {:<5} {:>8.2f}".format(palavra, encontrado, tempo))
print("Namedtuple - Tempo Médio: {:.2f} ms".format(calcular_tempo_medio(tempos_namedtuple_busca)))
print("")

def remover_palavras_especificas(container, palavras):
    inicio = time.time()
    for palavra in palavras:
        for idx, item in enumerate(container):
            if item.palavra == palavra:
                container.pop(idx)
                break
    fim = time.time()
    return (fim - inicio) * 1000  # Convertendo para milissegundos

print("TEMPO DE EXCLUSÃO".center(30))
print("Estrutura / Tempo Médio (ms)")

# Calcular tempo médio de exclusão das palavras específicas em cada estrutura de dados
tempo_medio_remocao_tupla_fixa = calcular_tempo_medio(pesquisar_palavras_especificas(tupla_container_fixa, palavras_especificas))
print("Tupla {:>10.2f} ms".format(tempo_medio_remocao_tupla_fixa))

tempo_medio_remocao_namedtuple = calcular_tempo_medio(pesquisar_palavras_especificas(namedtuple_container, palavras_especificas))
print("Namedtuple {:>5.2f} ms".format(tempo_medio_remocao_namedtuple))
