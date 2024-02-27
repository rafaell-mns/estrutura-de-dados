# Disponível em https://realpython.com/sorting-algorithms-python/#the-bubble-sort-algorithm-in-python

import time
from random import randint

def quicksort(array):
    if len(array) < 2:
        return array

    low, same, high = [], [], []
    pivot = array[randint(0, len(array) - 1)]

    for item in array:
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)

    return quicksort(low) + same + quicksort(high)

if __name__ == '__main__':

    while True:
        menu = '1 - 100k\n2 - 250k\n3 - 500k\n0 - Encerrar'
        print(menu)

        op = int(input("Digite a opção: "))

        if op == 1:
            caminho_arquivo = r'nomes100k.txt'
        elif op == 2:
            caminho_arquivo = r'nomes250k.txt'
        elif op == 3:
            caminho_arquivo = r'nomes500k.txt'
        elif op == 0:
            break
        else:
            print("Opção inválida")
        
        historico_tempo = []
        for i in range(10):
            with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
                lista_nomes = arquivo.read().splitlines()
            inicio = time.time()
            quicksort(lista_nomes)
            fim = time.time()

            timer = (fim - inicio) * 1000  
            historico_tempo.append(timer)

        for i, tempo in enumerate(historico_tempo):
            print(f'Execução {i+1}: {tempo:.2f}ms')

        media = sum(historico_tempo) / 10
        print(f'\nTempo médio: {media:.2f}ms')

