# def troca(s,velho,novo):
    # s=str(s)
    # velho=str(velho)
    # novo=str(novo)
    # s=s.replace(velho,novo)
    # print(s)
def troca(s, velho, novo):
    s = list(s)
    i = 0
    j = 0
    feito = False 
    while not feito:
        while (i < len(s)):
            while (j <= len(s)):
                if s[i:j] == list(velho):
                    s[i:j] = novo
                j += 1
            j = 0
            i  += 1
        feito = True
    s = ''.join(s) #Retira a lista de s e aspas
    print(s)
    return s
    
#codígo já executável,quando executa o arquivo
# s = input("Digite a palavra que deseja alterar : ")
# velho = input("Digite o termo que deseja alterar : ")
# novo = input("Digite o que deseja colocar no lugar de velho : ")
# s = troca(s, velho, novo)
# s = ''.join(s)
# print (s)
        
