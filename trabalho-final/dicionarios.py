import time
from collections import ChainMap, Counter, OrderedDict, defaultdict, UserDict

def ler_palavras(arquivo):
    with open(arquivo, 'r', encoding='utf-8') as f:
        return f.read().split()

def calcular_tempo(container, operacao, palavras):
    inicio = time.time()
    operacao(container, palavras)
    fim = time.time()
    return (fim - inicio) * 1000  # Convertendo para milissegundos

palavras_especificas = ["Lisbon", "NASA", "Kyunghee", "Konkuk", "Sogang", "momentarily", "rubella", "vaccinations", "government", "Authorities"]

def pesquisar_palavras_especificas(lista, palavras_especificas):
    tempos = []
    for palavra in palavras_especificas:
        inicio = time.time()
        encontrada, _ = pesquisar_palavra(palavra, lista)
        fim = time.time()
        tempo = (fim - inicio) * 1000  # Convertendo para milissegundos
        tempos.append(tempo)
    return tempos

def pesquisar_palavra(palavra, dicionario):
    tamanho = len(palavra)
    if tamanho in dicionario:
        if palavra in dicionario[tamanho]:
            return True, dicionario[tamanho].index(palavra)
    return False, -1

def inserir_em_dict(container, palavras):
    for palavra in palavras:
        tamanho = len(palavra)
        if tamanho not in container:
            container[tamanho] = []
        container[tamanho].append(palavra)

def remover_palavras_especificas(dicionario, palavras):
    inicio = time.time()
    for palavra in palavras:
        tamanho = len(palavra)
        if tamanho in dicionario and palavra in dicionario[tamanho]:
            dicionario[tamanho].remove(palavra)
    fim = time.time()
    return (fim - inicio) * 1000  # Convertendo para milissegundos

def imprimir_tempos(tempos, nome_container):
    for palavra, tempo, encontrada, _ in tempos:
        encontrado = "sim" if encontrada else "não"
        print("{:<12} {:<5} {:.2f} ms".format(palavra, encontrado, tempo))

arquivo = 'leipzig100k.txt'
palavras = ler_palavras(arquivo)

# Dicionário
dicionario_palavras = {}
tempo_dict = calcular_tempo(dicionario_palavras, inserir_em_dict, palavras)

#ChainMap
chainMap_palavras = ChainMap()
tempo_chainMap = calcular_tempo(chainMap_palavras, inserir_em_dict, palavras)

# Counter
counter_palavras = Counter()
tempo_counter = calcular_tempo(counter_palavras, inserir_em_dict, palavras)

# OrderedDict
ordered_dict_palavras = OrderedDict()
tempo_ordered_dict = calcular_tempo(ordered_dict_palavras, inserir_em_dict, palavras)

# defaultdict
default_dict_palavras = defaultdict(list)
tempo_default_dict = calcular_tempo(default_dict_palavras, inserir_em_dict, palavras)

# UserDict
class MyDict(UserDict):
    def inserir(self, palavras):
        for palavra in palavras:
            tamanho = len(palavra)
            if tamanho not in self.data:
                self.data[tamanho] = []
            self.data[tamanho].append(palavra)

user_dict_palavras = MyDict()
tempo_user_dict = calcular_tempo(user_dict_palavras, MyDict.inserir, palavras)

print("TEMPO DE INSERÇÃO".center(30))
print("Dicionário: {:>11.2f} ms".format(tempo_dict))
print("ChainMap: {:>13.2f} ms".format(tempo_chainMap))
print("Counter: {:>14.2f} ms".format(tempo_counter))
print("OrderedDict: {:>10.2f} ms".format(tempo_ordered_dict))
print("defaultdict: {:>11.2f} ms".format(tempo_default_dict))
print("UserDict: {:>14.2f} ms".format(tempo_user_dict))
print("")

print("TEMPO MÉDIO DE BUSCA".center(30))
print("Estrutura / Tempo Médio (ms)")

# Verificar tempo médio de pesquisa nas palavras específicas em cada estrutura de dados
tempos_dict = pesquisar_palavras_especificas(dicionario_palavras, palavras_especificas)
tempo_medio_dict = sum(tempos_dict) / len(tempos_dict) if tempos_dict else 0
print("{:<12} {:.2f}".format("Dicionário", tempo_medio_dict))

tempos_chainMap = pesquisar_palavras_especificas(chainMap_palavras, palavras_especificas)
tempo_medio_chainMap = sum(tempos_chainMap) / len(tempos_chainMap) if tempos_chainMap else 0
print("{:<12} {:.2f}".format("ChainMap", tempo_medio_chainMap))

tempos_counter = pesquisar_palavras_especificas(counter_palavras, palavras_especificas)
tempo_medio_counter = sum(tempos_counter) / len(tempos_counter) if tempos_counter else 0
print("{:<12} {:.2f}".format("Counter", tempo_medio_counter))

tempos_ordered_dict = pesquisar_palavras_especificas(ordered_dict_palavras, palavras_especificas)
tempo_medio_ordered_dict = sum(tempos_ordered_dict) / len(tempos_ordered_dict) if tempos_ordered_dict else 0
print("{:<12} {:.2f}".format("OrderedDict", tempo_medio_ordered_dict))

tempos_default_dict = pesquisar_palavras_especificas(default_dict_palavras, palavras_especificas)
tempo_medio_default_dict = sum(tempos_default_dict) / len(tempos_default_dict) if tempos_default_dict else 0
print("{:<12} {:.2f}".format("DefaultDict", tempo_medio_default_dict))

tempos_user_dict = pesquisar_palavras_especificas(user_dict_palavras.data, palavras_especificas)
tempo_medio_user_dict = sum(tempos_user_dict) / len(tempos_user_dict) if tempos_user_dict else 0
print("{:<12} {:.2f}".format("UserDict", tempo_medio_user_dict))
print("")

print("TEMPO MÉDIO DE EXCLUSÃO".center(30))
# Tempo de remoção das palavras específicas de cada estrutura de dados
tempo_remocao_dict = calcular_tempo(dicionario_palavras, remover_palavras_especificas, palavras_especificas)
tempo_remocao_chainMap = calcular_tempo(chainMap_palavras, remover_palavras_especificas, palavras_especificas)
tempo_remocao_counter = calcular_tempo(counter_palavras, remover_palavras_especificas, palavras_especificas)
tempo_remocao_ordered_dict = calcular_tempo(ordered_dict_palavras, remover_palavras_especificas, palavras_especificas)
tempo_remocao_default_dict = calcular_tempo(default_dict_palavras, remover_palavras_especificas, palavras_especificas)
tempo_remocao_user_dict = calcular_tempo(user_dict_palavras, remover_palavras_especificas, palavras_especificas)

print("Dicionário: {:>12.2f} ms".format(tempo_remocao_dict))
print("ChainMap: {:>15.2f} ms".format(tempo_remocao_chainMap))
print("Counter: {:>15.2f} ms".format(tempo_remocao_counter))
print("OrderedDict: {:>10.2f} ms".format(tempo_remocao_ordered_dict))
print("DefaultDict: {:>11.2f} ms".format(tempo_remocao_default_dict))
print("UserDict: {:>14.2f} ms".format(tempo_remocao_user_dict))
