from HashTable import HashTable

M = int(input("Insira o tamanho da tabela hash: "))
tab = HashTable(M)

# Seleciona a função hash
while True:
    funcao_hash = int(input("\nSelecione a função hash:\n1 - Letra inicial do nome\n2 - Fórmula que considera todos os caracteres do nome\nOpção: "))
    if(funcao_hash == 1 or funcao_hash == 2):
        break
    else:
        print("Opção inválida!\n")

# Insere os nomes do arquivo na tabela hash
with open('alunosED_2023.txt', 'r', encoding='utf-8') as file:
    lista_nomes = file.read().splitlines()

for nome in lista_nomes:
    tab.inserir(nome, funcao_hash)

print(f"\nNomes inseridos com sucesso na tabela hash com M = {M}.\n")

# Exibe o menu
while True:
    op = int(input("MENU:\n1 - Listar nomes\n2 - Número de colisões\n3 - Sair\nOpção: "))
    print("")

    if op == 1:    
        print(tab.listar())
    elif op == 2:
        print(tab.numero_colisoes(funcao_hash))
        media = len(lista_nomes)/M
        print(f"Número médio de colisões por índice {round(media, 2)}")
    elif op == 3:
        break
    else:
        print("Opção inválida!\n")
