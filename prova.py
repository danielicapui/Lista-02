#list.reverse() para 20 números
def lista_reverse():   
    list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    a=list[0]
    b=list[19]
    c=list[1]
    d=list[18]
    e=list[2]
    f=list[17]
    g=list[3]
    h=list[16]
    i=list[4]
    j=list[15]
    k=list[5]
    l=list[14]
    n=list[6]
    m=list[13]
    o=list[7]
    p=list[12]
    q=list[8]
    r=list[11]
    s=list[9]
    t=list[10]
    lista=[b,d,f,h,j,l,m,p,r,t,s,q,o,n,k,i,g,e,c,a]
    print(lista)
    for i in lista:
        print(i)
    return lista
#Segunda maneira de fazer usando o algoritmo de selectionsort
def selectionsort(lista):
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