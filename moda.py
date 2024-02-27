conjunto = []

N = int(input("Quantidade de dados: "))
print("Insira os dados:")

for i in range(N):
    conjunto.append(int(input()))

conjunto.sort()

sequencia_conjunto = []
numeros_repetidos = []

i = 0
while i < len(conjunto):
    numero_atual = conjunto[i]
    tamanho_sequencia = 1
    
    while i < len(conjunto) - 1 and conjunto[i] == conjunto[i + 1]: 
        tamanho_sequencia += 1 #se formar uma sequencia de numeros iguais, aumenta a variavel que controla isso
        i += 1

    sequencia_conjunto.append(tamanho_sequencia)
    numeros_repetidos.append(numero_atual)

    i += 1

amodal = True
multimodal = False
maior_sequencia = 1

for i in range(len(sequencia_conjunto)):
    if sequencia_conjunto[0] != sequencia_conjunto[i]:
        amodal = False #se os valores não tiverem frequências iguais, então existe moda no conjunto
    if sequencia_conjunto[i] > maior_sequencia:
        maior_sequencia = sequencia_conjunto[i] #atualiza o valor da maior frequência para determinar a moda
        moda_unica = numeros_repetidos[i]  #por enquanto a moda é esse valor

if not amodal:
    contador = 0
    for i in range(len(sequencia_conjunto)):
        if maior_sequencia == sequencia_conjunto[i]:
            contador += 1
        if contador > 1: #se existir 2 ou mais frequências iguais, ja tendo certeza que não é amodal, então o conjunto é multimodal
            multimodal = True

modas = []

if multimodal:
    for i in range(len(sequencia_conjunto)):
        if maior_sequencia == sequencia_conjunto[i]:
            modas.append(numeros_repetidos[i])

if amodal:
    print("Não existe moda no conjunto.")
elif len(modas) > 1:
    print("O conjunto é multimodal e as modas são:", modas)
else:
    print("O conjunto tem moda única:", moda_unica)