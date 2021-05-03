import os
import mysql.connector
from mysql.connector import Error
    
def exibeInformacoes(idcontato): #Pronta
    iniciaConexao()
    cursor.execute("select * from pessoas where id = '" + str(idcontato) + "';")
    linha = cursor.fetchone()
    terminaConexao()

    nome = 1
    email = 2
    nomeTwitter = 4
    nomeFacebook = 5
    nomeMySpace = 6
    nomeLinkedin = 7
    nomeInstagram = 8

    print("Nome: " + linha[nome])
    print("E-mail: " + linha[email])
    if linha[nomeTwitter] != '':
        print("Twitter: " + linha[nomeTwitter])
    if linha[nomeFacebook] != '':
        print("Facebook: " + linha[nomeFacebook])
    if linha[nomeMySpace] != '':
        print("MySpace: " + linha[nomeMySpace])
    if linha[nomeLinkedin] != '':
        print("Linkedin: " + linha[nomeLinkedin])
    if linha[nomeInstagram] != '':
        print("Instagram: " + linha[nomeInstagram])
 
def busca(text, tipo): #Pronta
    #Buscar contatos por nomes ou emails; 
    global idOrdenado
    idOrdenado = []
    contador = 0 
    idPessoa = 0
    nome = 1

    iniciaConexao()
    cursor.execute("select id, " + tipo +" from pessoas where " + tipo + " like '%" +  text + "%' order by nome;")
    linhas = cursor.fetchall()
    terminaConexao()
    
    for linha in linhas:
        print(str(contador) +" - " + linha[nome])
        idOrdenado.append(linha[idPessoa])
        contador = contador + 1

    print("")

def ordemAlfabetica(tipo): #Pronta
    #Organizar contato por ordem alfabética dos nomes, emails ou nome das redes sociais;
    global idOrdenado
    idOrdenado = []
    contador = 0 

    iniciaConexao()
    cursor.execute("select id, " + tipo + " from pessoas where "+ tipo +" != '' order by " + tipo + ";")
    linhas = cursor.fetchall()
    totalContatos = cursor.rowcount
    print(str(totalContatos) + " contatos encontrados que possuem um " + tipo + " \n")
    terminaConexao()

    idPessoa = 0
    nome = 1
    for linha in linhas:
        print(str(contador) +" - " + linha[nome])
        idOrdenado.append(linha[idPessoa])
        contador = contador + 1

    print("")

def ordenarPorGrupoDeInteresse(): #Pronta
    #Organizar contato por grupos de interesse.
    contador = 0
    global idOrdenado
    idOrdenado = []
    idPessoa = 0
    nome = 1

    iniciaConexao()
    cursor.execute("select id, nome from pessoas where grupoDeInteresse = 'familia' order by nome;")
    linhas = cursor.fetchall()
    print("Família:")
    for linha in linhas:
        print(str(contador) +" - " + linha[nome])
        idOrdenado.append(linha[idPessoa])
        contador = contador + 1

    cursor.execute("select id, nome from pessoas where grupoDeInteresse = 'amigos' order by nome;")
    linhas = cursor.fetchall()
    print("")
    print("Amigos:")        
    for linha in linhas:
        print(str(contador) +" - " + linha[nome])
        idOrdenado.append(linha[idPessoa])
        contador = contador + 1
    
    cursor.execute("select id, nome from pessoas where grupoDeInteresse = 'trabalho' order by nome;")
    linhas = cursor.fetchall()
    print("")
    print("Trabalho:")        
    for linha in linhas:
        print(str(contador) +" - " + linha[nome])
        idOrdenado.append(linha[idPessoa])
        contador = contador + 1

    terminaConexao()

def obtemVariavel(tipo): #Pronta
    while True:
        if tipo == "grupoDeInteresse":
            while True:
                text = input(tipo + "(amigos, familia, trabalho): ")
                text = text.lower()
                if text == "amigos" or text == "familia" or text == "trabalho":
                    break
                else:
                    print("ERRO: O campo " + tipo + " deve conter somente uma das opçães (amigos, familia, trabalho) !!!")
                    print("")
        else:
            text = input(tipo + "*: ")

        if text == "":
            print("ERRO: O campo " + tipo +" é OBRIGATÓRIO!")
        else:
            break
    return text

def obtemVariavelOpcional(tipo): #Pronta
    text = input(tipo + ": ")
    return text

def adicionaContato(): #Pronta
    iniciaConexao()
    print("Legenda: * Obrigatória")
    cursor.execute("insert into pessoas values (default,'" + obtemVariavel("nome") + "','" + obtemVariavel("email") +"','"+ obtemVariavel("grupoDeInteresse")+"','"+obtemVariavelOpcional("nomeTwitter")+"','"+obtemVariavelOpcional("nomeFacebook")+"','"+ obtemVariavelOpcional("nomeMySpace")+"','"+ obtemVariavelOpcional("nomeLinkedin")+"','"+ obtemVariavelOpcional("nomeInstagram")+"');")

    con.commit()
    print(str(cursor.rowcount) + " contatos inseridos com sucesso!!!")
    terminaConexao()

def menu(mensagem): #Pronta
    if mensagem != "":
        print(mensagem)

    print("------MENU------")
    print("1 - Exibir contatos")
    print("2 - Buscar contato")
    print("3 - Adicionar contato")
    print("4 - Sair")
    opcao = int(input("Escolha uma opção: "))
    
    os.system('cls')
    
    if opcao == 1: #Exibir contatos
        print("------MENU -> EXIBIÇÃO------")
        print("1 - Ordem alfabética")
        print("2 - Ordenar por grupos de interesse ")
        opcaoExibicao = int(input("Escolha um modo de exibição: "))

        if opcaoExibicao == 1:
            os.system('cls')

            print("------MENU -> EXIBIÇÃO -> ORDEM ALFABÉTICA------")
            print("1- por nome")
            print("2- por E-mail")
            print("3- por nome do Twitter")
            print("4- por nome do Facebook")
            print("5- por nome do MySpace")
            print("6- por nome do Linkedin")
            print("7- por nome do Instagram")
            opcaoAlfabetica = int(input("Escolha por qual parametro deseja ordenar alfabéticamente: "))
            
            os.system('cls')

            if opcaoAlfabetica <= 7 and opcaoAlfabetica >= 1:
                if opcaoAlfabetica == 1:
                    print("------MENU -> EXIBIÇÃO -> ORDEM ALFABÉTICA -> NOME------")
                    ordemAlfabetica("nome")
                elif opcaoAlfabetica == 2:
                    print("------MENU -> EXIBIÇÃO -> ORDEM ALFABÉTICA -> E-MAIL------")
                    ordemAlfabetica("email")
                elif opcaoAlfabetica == 3:
                    print("------MENU -> EXIBIÇÃO -> ORDEM ALFABÉTICA -> TWITTER------")
                    ordemAlfabetica("nomeTwitter")
                elif opcaoAlfabetica == 4:
                    print("------MENU -> EXIBIÇÃO -> ORDEM ALFABÉTICA -> FACEBOOK------")
                    ordemAlfabetica("nomeFacebook")
                elif opcaoAlfabetica == 5:
                    print("------MENU -> EXIBIÇÃO -> ORDEM ALFABÉTICA -> MYSPACE------")
                    ordemAlfabetica("nomeMySpace")
                elif opcaoAlfabetica == 6:
                    print("------MENU -> EXIBIÇÃO -> ORDEM ALFABÉTICA -> LINKEDIN------")
                    ordemAlfabetica("nomeLinkedin")
                elif opcaoAlfabetica == 7:
                    print("------MENU -> EXIBIÇÃO -> ORDEM ALFABÉTICA -> INSTAGRAM------")
                    ordemAlfabetica("nomeInstagram")

                while True:
                    indiceDoidOrdenado = int(input("Escolha um contato para exibir informaçãoes: "))
                    if indiceDoidOrdenado < len(idOrdenado) and indiceDoidOrdenado >= 0:
                        print("")
                        exibeInformacoes(idOrdenado[indiceDoidOrdenado])
                        break
                    else:
                        print("ERRO: OPÇÃO INEXISTENTE!!!")
            else:
                print("ERRO: OPÇÃO INEXISTENTE!!!")
                
            
        elif opcaoExibicao == 2:
            os.system('cls')

            print("------MENU -> EXIBIÇÃO -> GRUPOS DE INTERESSE------")
            ordenarPorGrupoDeInteresse()
            print("")

            while True:
                indiceDoidOrdenado = int(input("Escolha um contato para exibir informaçãoes: "))
                if indiceDoidOrdenado < len(idOrdenado) and indiceDoidOrdenado >= 0:
                    print("")
                    exibeInformacoes(idOrdenado[indiceDoidOrdenado])
                    break
                else:
                    print("ERRO: OPÇÃO INEXISTENTE!!!")

        else:
            print("ERRO: OPÇÃO INEXISTENTE!!!")
            
    elif opcao == 2:  #Buscar contato
        print("------MENU -> BUSCA------")
        print("1 - Buscar nome")
        print("2 - Buscar e-mail ")

        opcaoBusca = int(input("Escolha um modo de busca:"))
        
        os.system('cls')
        print("------MENU -> BUSCA -> RESULTADO------")

        if opcaoBusca == 1:
            busca(input("Digite o nome: "), "nome")
        elif opcaoBusca == 2:
            busca(input("Digite o e-mail: "), "email")
        else:
            print("ERRO: OPÇÃO INEXISTENTE!!!")

        
        while True:
            indiceDoidOrdenado = int(input("Escolha um contato para exibir informaçãoes: "))
            if indiceDoidOrdenado < len(idOrdenado) and indiceDoidOrdenado >= 0:
                print("")
                exibeInformacoes(idOrdenado[indiceDoidOrdenado])
                break
            else:
                print("ERRO: OPÇÃO INEXISTENTE!!!")
   
    elif opcao == 3: #Adicionar contato
        print("------MENU -> ADICIONAR CONTATO ------")
        adicionaContato()

    elif opcao == 4: #Sair
        global continua
        if con.is_connected():
            while True:
                cursor.close()
                con.close()
                if False == con.is_connected():
                    print("Conexão ao MySQL foi encerrada")
                    continua = False
                    print("Programa encerrado!!!")
                    break
                else:
                    print("ERRO: Conexão não foi encerrada!!!")
        else: 
            continua = False
            print("Programa encerrado!!!")
    
    else:
        print("ERRO: OPÇÃO INEXISTENTE!!!")

def pause(): #Pronta
    #função que criei por que o os.system('pause') não tava funcionando no Trinket
    nada = input("Pressione ENTER para continuar...")

def iniciaConexao(): #Pronta
    global con
    global cursor
    
    #Altere as informações do seu servidor MySQL aqui
    con = mysql.connector.connect(host='localhost', database='contatos', user='root', password='suaSenha')
    cursor = con.cursor()
    
def terminaConexao(): #Pronta
    if con.is_connected():
        cursor.close()
        con.close()

iniciaConexao()
if con.is_connected():
    alerta = ("Conectado as servidos MySQL versão " + str(con.get_server_info()))
    cursor.execute("select database();")
    linha = cursor.fetchone()
    alerta = alerta + ("\nConectado ao banco de dados '" + str(linha[0])+"'")
terminaConexao()

print("")

continua = True
while continua:
    os.system('cls')
    menu(alerta)
    if continua:
        print("")
        pause()




