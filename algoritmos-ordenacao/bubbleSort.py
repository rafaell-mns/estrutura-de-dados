# Disponível em https://www.geeksforgeeks.org/python-program-for-bubble-sort/

import time

def bubbleSort(arr):
    n = len(arr)
    # optimize code, so if the array is already sorted, it doesn't need
    # to go through the entire process
    swapped = False
    # Traverse through all array elements
    for i in range(n-1):
        # range(n) also work but outer loop will
        # repeat one time more than needed.
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
         
        if not swapped:
            # if we haven't needed to make a single swap, we 
            # can just exit the main loop.
            return

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
            bubbleSort(lista_nomes)
            fim = time.time()

            timer = (fim - inicio)
            historico_tempo.append(timer)
            print(f"Execução {i} tempo: {timer}.")

        for i, tempo in enumerate(historico_tempo):
            print(f'Execução {i+1}: {tempo:.2f}s')

        media = sum(historico_tempo) / 10
        print(f'\nTempo médio: {media:.2f}s')