#Matriz1 
def build_matriz1 (linhas1, colunas1):#função que cria uma matriz.
    matriz1 = [] #define a matriz.
    for i in range(1, linhas1+1): #um laço para colocar valores na função.
        d = []    #matriz auxiliar
        for j in range (1, colunas1+1): #laço para pegar valores e colocar na matriz.
            x = int(input("Digite o elementro m%i%i da matriz:" % (i,j)))
            d.append(x) #pega valores digitados no input x
            matriz1.append(d) #coloca valores na matriz
    print(40*'=') #Imprimi 40 iguais para separa a função
    print("Matriz1:\n",matriz1)
    print(40*'=')
    return matriz1
#Matriz2 mesma essência que build_matriz1, mas por motivos estratégicos fiz outra função para usar n%i%j
def build_matriz2(linhas2,colunas2):
    matriz2=[]
    for e in range(1, linhas2+1):
        f = []
        for g in range (1, colunas2+1):
            y = int(input("Digite o elementro n%i%i da matriz:" % (e,g)))
            f.append(y)
            matriz2.append(f)
    print(40*'=')
    print("Matriz2:\n",matriz2)
    print(40*'=')
    return matriz2

def sum_matriz(m1, m2): #função soma de matrizes.
    matriz_soma = [] #define matriz resultante.
    conta_linhas = len(m1) # Conta quantas linhas existem
    conta_colunas = len(m1[0]) # Conta quantos elementos têm em uma linha
    for i in range(conta_linhas): #para cada linha na matriz pega e adiciona na matriz_soma
        # Cria uma nova linha na matriz_soma
        matriz_soma.append([])
        for j in range(conta_colunas): #para cada coluna.
            # Soma os elementos que possuem o mesmo índice
            soma = m1[i][j] + m2[i][j] #pega os mesmo valores posicionais da matriz1 e matriz 2
            matriz_soma[i].append(soma) #coloca os valores na matriz_soma
    return matriz_soma #retorna a matriz_soma
print(40*'=')
print("Matriz soma:",sum_matriz(build_matriz1(4,4),build_matriz2(4,4))) #realiza e imprimi a função soma para a matriz1 e 2  com linhas/colunas 4x4.
print(40*'=')
#Implementado por Daniel Lucas.