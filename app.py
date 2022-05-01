from main import metodosEInicializacao as metodos

def opcaoMaior(mainClass):
    opcao = 0
    while(opcao <= 6 and opcao >= 0):
        print("Digite a opcao do programa: (0 para sair)")
        print("1. Retornar tweet com mais engajamento " 
        +"\n 2. Retornar tweet com mais impressoes "
        +"\n 3. Retornar tweet com mais retweets"
        +"\n 4. Retornar tweet com mais respostas"
        +"\n 5. Retornar tweet com mais favoritos"
        +"\n 6. Retornar tweet com mais cliques no perfil"
        +"\n 0. Voltar ao menu")
        opcao = int(input())

        if(opcao == 1):
            mainClass.maiorGenerico(mainClass.listaTweetsCompletos,'engajamentos')
        elif(opcao == 2):
            print(mainClass.maiorGenerico(mainClass.listaTweetsCompletos,"impressoes"))
        elif(opcao == 3):
            print(mainClass.maiorGenerico(mainClass.listaTweetsCompletos,"retweets"))
        elif(opcao == 4):
            print(mainClass.maiorGenerico(mainClass.listaTweetsCompletos,"respostas"))
        elif(opcao == 5):
            print(mainClass.maiorGenerico(mainClass.listaTweetsCompletos,"favoritos"))
        elif(opcao == 6):
            print(mainClass.maiorGenerico(mainClass.listaTweetsCompletos,"cliquesNoPerfil"))
        elif(opcao == 0):
             return 

def opcaoMaiorHorario(mainClass):
    tuplaHorarios = mainClass.formataHorarios(mainClass.listaTweetsCompletos)
    listaHorarios = tuplaHorarios[0]
    listaTweetsHorarios = tuplaHorarios[1]
    opcao = 0
    while(opcao <= 8 and opcao >= 0):
        print("Digite a opcao do programa: (0 para sair)")
        print("1. Retornar quantidade de tweets por horario " 
        +"\n 2. Retornar horario com mais tweets(horario que mais posta) "
        +"\n 3. Retornar horario com mais engajamentos"
        +"\n 4. Retornar horario com mais impressoes"
        +"\n 5. Retornar horario com mais retweets"
        +"\n 6. Retornar horario com mais respostas"
        +"\n 7. Retornar horario com mais favoritos"
        +"\n 8. Retornar horario com mais cliques no perfil"
        +"\n 0. Voltar ao menu")
        opcao = int(input())

        if(opcao == 1):
            for i in range (0,len(listaHorarios)):
                print("Horario: ", i, "Numero de tweets: ",listaHorarios[i])
        elif(opcao == 2):
            resultado = mainClass.horarioComMaisTweets(listaHorarios)
            print("Horario com mais tweets: ",resultado[0],"Numeros de tweets desse horario: ", resultado[1],"Total de tweets do mes: ",resultado[2])
        if(opcao == 3):
            resultado = mainClass.horarioComMaisGenerico(listaHorarios,listaTweetsHorarios,'engajamentos')
            print("Horario com mais engajamento: ",resultado[0],"Porcentagem de engajamentos: ","{:.2%}".format(resultado[1]))
        elif(opcao == 4):
            resultado = mainClass.horarioComMaisGenerico(listaHorarios,listaTweetsHorarios,'impressoes')
            print("Horario com mais impressoes: ",resultado[0],"Porcentagem de impressoes: ","{:.2%}".format(resultado[1]))
        elif(opcao == 5):
            resultado = mainClass.horarioComMaisGenerico(listaHorarios,listaTweetsHorarios,'retweets')
            print("Horario com mais retweets: ",resultado[0],"Porcentagem de retweets: ","{:.2%}".format(resultado[1]))
        elif(opcao == 6):
            resultado = mainClass.horarioComMaisGenerico(listaHorarios,listaTweetsHorarios,'respostas')
            print("Horario com mais respostas: ",resultado[0],"Porcentagem de respostas: ","{:.2%}".format(resultado[1]))
        elif(opcao == 7):
            resultado = mainClass.horarioComMaisGenerico(listaHorarios,listaTweetsHorarios,'favoritos')
            print("Horario com mais favoritos: ",resultado[0],"Porcentagem de favoritos: ","{:.2%}".format(resultado[1]))
        elif(opcao == 8):
            resultado = mainClass.horarioComMaisGenerico(listaHorarios,listaTweetsHorarios,'cliquesNoPerfil')
            print("Horario com mais cliques no perfil: ",resultado[0],"Porcentagem de cliques no perfil: ","{:.2%}".format(resultado[1]))
        elif(opcao == 0):
             return 

def menu():

    mainClass = metodos()
    #print(mainClass.listaTweetsCompletos)

    opcao = 0
    while(opcao <= 4 and opcao >= 0):
        print("Digite a opcao do programa: (0 para sair)")
        print("1. Listar todos os tweets " 
        +"\n 2. Opcoes com engajamentos e impressoes "
        +"\n 3. Opcoes em relacao a horarios"
        +"\n 4. Opcoes com relacao a pesquisa de palavras/usuarios"
        +"\n 0. Sair")
        opcao = int(input())

        if(opcao == 0):
            print("programa finalizado!")
            exit()
        if(opcao == 1):
            for tweets in mainClass.listaTweetsCompletos:
                tweets.funcRetorno()
        if(opcao == 2):
            opcaoMaior(mainClass)
        if(opcao == 3):
            opcaoMaiorHorario(mainClass)
        if(opcao == 4):
            print("n implementado")
menu()