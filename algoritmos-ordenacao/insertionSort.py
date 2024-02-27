# Disponível em https://www.geeksforgeeks.org/python-program-for-insertion-sort/?ref=lbp

import time

def insertionSort(arr):
    n = len(arr)  # Get the length of the array
      
    if n <= 1:
        return  # If the array has 0 or 1 element, it is already sorted, so return
 
    for i in range(1, n):  # Iterate over the array starting from the second element
        key = arr[i]  # Store the current element as the key to be inserted in the right position
        j = i-1
        while j >= 0 and key < arr[j]:  # Move elements greater than key one position ahead
            arr[j+1] = arr[j]  # Shift elements to the right
            j -= 1
        arr[j+1] = key  # Insert the key in the correct position

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
            insertionSort(lista_nomes)
            fim = time.time()

            timer = (fim - inicio)
            historico_tempo.append(timer)
            print(f"Execução {i+1} tempo: {timer}.")

        for i, tempo in enumerate(historico_tempo):
            print(f'Execução {i+1}: {tempo:.2f}s')

        media = sum(historico_tempo) / 10
        print(f'\nTempo médio: {media:.2f}s')