def cadastro():
    l=cadastrados()
    nome=input("Digite o seu nome:\n ")
    email=input("Digite o seu e-mail:\n")
    login=input("Digite o seu login:\n")
    senha=input("Digite sua senha:\n")
    tipo=input("Digite se você é professor ou aluno:\n")
    adiciona(pessoa(nome,email,login,senha,tipo),l)
    return l 
    

def pessoa(n,e,l,p,t):
    return {'nome':n,
    'email': e,
    'login' :l,
    'senha': p,
    'tipo':t}

def adiciona(p, l):
    l.append(p)
    return l
# s=cadastro()
# print(s)
usuarios = [{"Nome":"Daniel Lucas","E-mail":"daniel.icapui@hotmail.com","Login":"akeno_misaki","senha":"haifuri","Tipo":"aluno"},
    {"Nome":"Alysson","E-mail":"alysson.uern@hotmail.com","Login":"alyssonuern","senha":"uern1234","Tipo":"professor"}]

def cadastrados():
    return usuarios
def professores():
     l=cadastrados()
     count=0
     a="professor"
     docente=[]
     while count<=len(l):
            c=l[count-1]["Tipo"]
            if a==c:      
                docente.append(c)
            count +=1
     return docente
def alunos():
     l=cadastrados()
     count=0
     b="aluno"
     discente=[]
     while count<=len(l):
            c=l[count-1]["Tipo"]
            if b==c:      
                discente.append(c)
            count +=1
     return discente

#tentar definir uma variaavel para usa-la de refencia na interface como logado#priodiade máxima
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
            return logado
    else:
        opcao=int(input("Senha ou login errado tente de novo\nDigite 1 para tentar de novo ou 2 para mudar senha:"))
        if opcao==1:
            login()
        elif opcao==2:
            recover()
            login()
#retornar algum valor
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
                    return l
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
    world=int(input("Para se cadastrar digite 1:\n Para login digite 2:\n"))
    if world==1:
            a=cadastro()
            return a
    elif world==2:
            b=login()
            return b
    else:
            print("Opção inválida,desligando...")
            exit()
def mostra_lista(l):
    for m in l:
        print(40* '=')
        for k,v in m.items():
            print("{}: {}".format(k.capitalize(),v))
    print(40* '=')
def loginoff():
    exit()
l_idiomas=[{"alemao":1},{"espanhol":2},{"frances":3},{"ingles":4},{"japones":5},{"madarim":6},{"portugues":7},{"russo":8}]
def idiomas():
    return l_idiomas

l_horarios=[{"manha":1},{"tarde":2},{"noite":3}]
def horarios():
    return l_horarios
#completar lista
l_dias=[{"segunda":1},{"terca":2},{"quarta":3},{"quinta":4},{"sexta":5}]
def dias():
    return l_dias

def notas(discente,nota):
    alunos()
    discente=[{}]
    discente.append(nota)
    return discente

def faltas()
#falta completar item com listas 4,5,6 e adiciona funções para colocar horários ,idiomas,dias para os usuarios tipo aluno para professores falta criar uma função de cadatrar notas,faltas e ver disciplinas que ministra.Além disso tem que definir um fluxo helloworld,cadastro ou login,interface.Todas as funções devem ter seus dados disponiveis para serem usados pela função interface
def interface(): 
    cadastrados()
    helloworld()
    idiomas()
    horarios()
    notas()
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
                    mostra_lista(l_idiomas)
                    opcao=int(input("Digite os idiomas que pretende estudar:\n"))
                    #melhorar o sistema para adicionar materias ao usuario logado
                    adiciona(opcao,l)
                if op == '2':
                    mostra_lista(l_horarios)
                    opcao=int(input("Escolhar seu horário que deseja estudar:\n"))
                    #melhorar o sistem para adicionar dias e horarios ao usuario logado
                    adiciona(opcao,l)
                
                if op == '3':
                    #definir e consultar cidade e estado onde o curso será realizadoo

                if op == '4':
                    alunos()
                    print(notas)
                    opcao=input("Deseja cadastrar notas (y\n)")
                    if opcao=='y':
                        nota=int(input("Digite a nota que você quer colocar:\n"))
                        print(discente)
                        tipo=input(("Digite ao usuario ao qual você quer colocar a nota"))
                        count=0
                        while count<=len(l):
                            aluno=l[count-1]["Login"]
                            if aluno==tipo:
                                notas(tipo,nota)
                                print(notas)
                                break
                            else:       
                                count +=1
                    elif opcao=='n':
                        print("Voltando ao menu")
                    else:
                        print("Opção inválida")
                    #criar uma função para cadastrar notas de usuarios tipo alunos

                if op=='5':
                    #criar uma função para cadastrar faltas e exibir de usuarios tipo alunos
                if op=='6':
                    #criar uma função para mostrar as diciplinas que este professor ministra
                if op=='7':
                    loginoff()
if __name__=='__sistema__':
    interface()
#chamar a função interface e todas as subfunções devem funcionar seguidamente com seus dados
interface()


