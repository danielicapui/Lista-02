def cadastro():
    l=cadastrados()
    nome=input("Digite o seu nome:\n ")
    email=input("Digite o seu e-mail:\n")
    login=input("Digite o seu login:\n")
    senha=input("Digite sua senha:\n")
    tipo=input("Digite se você é professor ou aluno:\n")
    p=[{"Nome":nome,"E-mail":email,"Login":login,"Senha":senha,"Tipo":tipo}]
    l.append(p)
    return l
def pessoa(n,e,l,p):
    return {'nome':n,
    'email': e,
    'login' :l,
    'senha': p}
def adiciona(p, l):
    l.append(p)
    return l
# s=cadastro()
# print(s)
usuarios = [{"Nome":"Daniel Lucas","E-mail":"daniel.icapui@hotmail.com","Login":"akeno_misaki","senha":"haifuri","Tipo":"aluno"},
    {"Nome":"Alysson","E-mail":"alysson.uern@hotmail.com","Login":"alyssonuern","senha":"uern1234","Tipo":"professor"}]
def cadastrados():
    return usuarios

def login(): 
    l=cadastrados()
    # print(l)
    # login=l[0]["Login"]
    # senha=l[0]["senha"]
    count=0
    mundo=False
    usuario=input("digite o usuario")
    password=input("digite a sua senha")
    while count<=len(l):
        login=l[count-1]["Login"]
        senha=l[count-1]["senha"]
        if login==usuario and senha==password:
            mundo=True
            break
        else:       
            count +=1
    if mundo==True:
        interface()
    else:
        opcao=int(input("Senha ou login errado tente de novo\nDigite 1 para tentar de novo ou 2 para mudar senha:"))
        if opcao==1:
            login()
        elif opcao==2:
            recover()
def recover():           
            l=cadastrados()
            mundo=False
            seuemail=input("Digite o seu email:\n")
            count=0
            while mundo==False:    
                while count<=len(l):
                    email=l[count-1]["E-mail"]
                    if seuemail==email:
                        mundo=True
                        break
                        break
                    else:       
                        count +=1
                if mundo==True:
                    print("E-mail correto")
                    novasenha=input("Digite sua nova senha:\n")
                    l[count-1]["senha"] = novasenha
                    print("Senha atualizada com sucesso, Voltando para tela de login.")
                    login()
                    break
                    break
                else:
                    escolha=input("E-mail errado ,deseja tentar novamente? (y/n)")
                    if escolha=="y":
                        mundo==False
                        
                    else:
                        mundo==True
                    
                
            
def helloworld():
    # t=text(text='Bem vindo ao sistema de ensino de idiomas', align='center' ,color=color.blue)
    world=int(input("Para se cadastrar digite 1\n Para login digite 2:\n"))
    if world==1:
            cadastro()
        
    if world==2:
            login()
    else:
            print("Opção inválida,desligando...")
            exit()
def mostra_lista(l):
    for m in l:
        print(40* '=')
        for k,v in m.items():
            print("{}: {}".format(k.capitalize(),v))
    print(40* '=')

def interface(): 
    l_idiomas=[{"alemao":1},{"espanhol":2},{"frances":3},{"ingles":4},{"japones":5},{"madarim":6},{"portugues":7},{"russo":8}]
    while True:
                op = input("""
    1) Para Alunos:Cadastrar ou consultar os idiomas que pretende estudar.
    2) Para Alunos:Cadastrar e Consultar o horário e o dia que melhor pode frequentar a escola.
    3) Para Alunos:Cadastrar e consultar o local (cidade e estado) onde pretende realizar o curso.
    4) Para Professor:Cadastrar notas de alunos.
    5)Para Professor:Número de faltas dos alunos.
    6)Para Professor:As disciplinas que ministra.
    7)Login off
        Escolha uma opção: """)
                if op == '1':
                    print("cadastros")
                if op == '2':
                    mostra_lista(l_clientes)
                
                if op == '3':
                    mostra_lista(l_funcionarios)
                    mostra_lista(l2_funcionarios)

                if op == '4':
                    exit()

                if op=='5':
                    mostra_lista(l_serv)
                    servico=int(input("Digite o serviço desejado:"))
                    if servico>=1 and servico<=7:
                        print("No momento o serviço está fora de circulação, tente novamente em outra hora")
                        info=int(input("Para mais informações digite 2:"))
                        if info==2 :
                                 print("Os serviços não estão funcionando devido a falta de funcionarios, se você tiver em interesse em trabalhar conosco volte para o menu inicial e digite 6")
                        else:
                                 print("Voltando ao menu")
                if op=='6':
                    nome = input("Digite o seu nome: ")
                    sexo= input("Digite o seu sexo? (homem/mulher): ")
                    cart= input("Digite o numero da sua carteira: ")
                    funcao=input("Digite sua função programador(a) ou designer") 
                    adiciona_pessoa(programador(nome,sexo, cart,funcao), l2_funcionarios)
if __name__=='__sistema__':
    interface()
entrar=helloworld()
