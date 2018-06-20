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
    Done = False
    while not Done:
        while (i < len(s)):
            while (j <= len(s)):
                if s[i:j] == list(velho):
                    s[i:j] = novo
                j += 1
            j = 0
            i  += 1
        Done = True
    s = ''.join(s) #Retira a lista de s e aspas
    return s
    print(s)
#codígo já executável

        
