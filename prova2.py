def vetor(n):
    # q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17,q18,q19,q20,q21,q22,q23,q24,q25 =[int(x) for x in input("Digite elementos linha1:\n").split()]
    lista=[]
    for j in range (1,n+1):
        x = int(input("Digite o elemento do vetor:")) 
        lista.append(x)
    return lista
def selectionsort(lista):#ordena a lista
   for i in range(len(lista)-1,0,-1):
       posicaomax=0
       for localizacao in range(1,i+1):
           if lista[localizacao]>lista[posicaomax]:
               posicaomax = localizacao
       aux = lista[i]
       lista[i] = lista[posicaomax]
       lista[posicaomax] = aux
   print(lista)
   return(lista)

def getmaxv(lista):#pega valor mínimo e máximo
    selectionsort(lista) 
    max=lista[-1]
    return max
def getminv(lista):
    selectionsort(lista) 
    min=lista[0]
    return min
def soma_lista(lista):#soma os elementos da matriz
    soma = 0
    for i in range(len(lista)):
        soma += lista[i]
    return soma
def media_lista(lista): #retorna a média
    media=(soma_lista(lista) / len(lista) )
    return media
def desvio(lista):#retorna o desvio padrão
    media = media_lista(lista)
    x = 0
    for elemento in lista:
        x = float(x) + float((float(elemento) - float(media))**2)
        variancia = x/len(lista)
    desvio = variancia**(0.5)
    return (desvio)
#Valores predefinidos
f=vetor(25) 
print("Valor de máximo:\n {} \n Valor de mínimo\n {}".format(getmaxv(f),getminv(f)))
print("Média:\n",media_lista(f))
print("Desvio padrão:\n",desvio(f))

if __name__=='__prova2__':
    vetor()
