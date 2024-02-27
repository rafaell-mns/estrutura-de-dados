# Disponível em https://www.geeksforgeeks.org/python-program-for-shellsort/

import time

def shellSort(arr):
 
    # Start with a big gap, then reduce the gap
    n = len(arr)
    gap = n//2
 
    # Do a gapped insertion sort for this gap size.
    # The first gap elements a[0..gap-1] are already in gapped
    # order keep adding one more element until the entire array
    # is gap sorted
    while gap > 0:
 
        for i in range(gap,n):
 
            # add a[i] to the elements that have been gap sorted
            # save a[i] in temp and make a hole at position i
            temp = arr[i]
 
            # shift earlier gap-sorted elements up until the correct
            # location for a[i] is found
            j = i
            while j >= gap and arr[j-gap] >temp:
                arr[j] = arr[j-gap]
                j -= gap
 
            # put temp (the original a[i]) in its correct location
            arr[j] = temp
        gap //= 2
 

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
            shellSort(lista_nomes)
            fim = time.time()

            timer = (fim - inicio) * 1000  
            historico_tempo.append(timer)

        for i, tempo in enumerate(historico_tempo):
            print(f'Execução {i+1}: {tempo:.2f}ms')

        media = sum(historico_tempo) / 10

        print(f'\nTempo médio: {media:.2f}ms')