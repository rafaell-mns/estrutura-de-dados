# Disponível em https://www.geeksforgeeks.org/python-program-for-selection-sort/

import time

def selectionSort(array, size):
    
    for ind in range(size):
        min_index = ind
 
        for j in range(ind + 1, size):
            # select the minimum element in every iteration
            if array[j] < array[min_index]:
                min_index = j
         # swapping the elements to sort the array
        (array[ind], array[min_index]) = (array[min_index], array[ind])
 

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
            selectionSort(lista_nomes, len(lista_nomes))
            fim = time.time()

            timer = (fim - inicio)
            historico_tempo.append(timer)
            print(f"Execução {i+1} tempo: {timer}.")

        for i, tempo in enumerate(historico_tempo):
            print(f'Execução {i+1}: {tempo:.2f}s')

        media = sum(historico_tempo) / 10
        print(f'\nTempo médio: {media:.2f}s')