import pandas as pd
import re
from re import search
from classeInicial import idtextoTweet as idT #id + texto
from classeFinal import tweetCompleto as tC #tweet completo(classe com mais dados)

class metodosEInicializacao:
    def __init__(self):
        tabela = pd.read_csv('tweet_activity_metrics_vayno_20220312_20220409_pt.csv')
        #print(tabela)
        tabela = tabela.drop(["id do Tweet"], axis=1) #remove a coluna com nome ___ 
        tabela = tabela.drop(["cliques no URL"], axis=1)
        tabela = tabela.drop(["cliques em hashtags:"], axis=1)
        tabela = tabela.drop(["expansões de detalhes:"], axis=1)
        tabela = tabela.drop(["cliques no link permanente"], axis=1)
        tabela = tabela.drop(["aberturas de aplicativos"], axis=1)
        tabela = tabela.drop(["instalações de aplicativo:"], axis=1)
        tabela = tabela.drop(["seguiram"], axis=1)
        tabela = tabela.drop(["Tweet enviado por e-mail"], axis=1)
        tabela = tabela.drop(["número de telefone discado"], axis=1)
        tabela = tabela.drop(["visualizações da mídia"], axis=1)
        tabela = tabela.drop(["engajamentos com mídia"], axis=1)
        tabela = tabela.drop(["impressões promovido(a)(s)"], axis=1)
        tabela = tabela.drop(["engajamentos promovido(a)(s)"], axis=1)
        tabela = tabela.drop(["taxa de engajamento promovido(a)(s)"], axis=1)
        tabela = tabela.drop(["retweets promovido(a)(s)"], axis=1)
        tabela = tabela.drop(["respostas promovido(a)(s)"], axis=1)
        tabela = tabela.drop(["favoritos promovido(a)(s)"], axis=1)
        tabela = tabela.drop(["cliques no perfil do usuário: promovido(a)(s)"], axis=1)
        tabela = tabela.drop(["cliques no URL promovido(a)(s)"], axis=1)
        tabela = tabela.drop(["cliques em hashtags: promovido(a)(s)"], axis=1)
        tabela = tabela.drop(["expansões de detalhes: promovido(a)(s)"], axis=1)
        tabela = tabela.drop(["cliques no link permanente promovido(a)(s)"], axis=1)
        tabela = tabela.drop(["aberturas de aplicativos promovido(a)(s)"], axis=1)
        tabela = tabela.drop(["instalações de aplicativo: promovido(a)(s)"], axis=1)
        tabela = tabela.drop(["seguiram promovido(a)(s)"], axis=1)
        tabela = tabela.drop(["Tweet enviado por e-mail promovido(a)(s)"], axis=1)
        tabela = tabela.drop(["número de telefone discado promovido(a)(s)"], axis=1)
        tabela = tabela.drop(["visualizações da mídia promovido(a)(s)"], axis=1)
        tabela = tabela.drop(["engajamentos com mídia promovido(a)(s)"], axis=1)
        #tabela = tabela.dropna(how= 'all', axis=1)
        #print(tabela)

        # converting column data to list
        linkPermanenteList = tabela['link permanente do Tweet'].tolist()
        textoDoTweetList = tabela['texto do Tweet'].tolist()
        horarioList = tabela['horário'].tolist()
        impressoesList = tabela['impressões'].tolist()
        engajamentosList = tabela['engajamentos'].tolist()
        retweetsList = tabela['retweets'].tolist()
        respostasList = tabela['respostas'].tolist()
        favoritosList = tabela['favoritos'].tolist()
        cliquesPerfilList = tabela['cliques no perfil do usuário:'].tolist()

        
        # printing list data
        '''
        print('link permanente do Tweet:', linkPermanente)
        print('texto do Tweet:', textoDoTweet)
        print('horário:', horario)
        print('impressões:', impressoes)
        print('engajamentos:', engajamentos)
        print('retweets:', retweets)
        print('respostas:', respostas)
        print('favoritos:', favoritos)
        print('cliques no perfil do usuário:', cliquesPerfil)
        '''

        ##adiciona as structs de tweet a um array
        listaTweetsCompletos = []

        for i in range(0,len(linkPermanenteList)):
            tweetMontagem = tC(linkPermanenteList[i],textoDoTweetList[i],horarioList[i],impressoesList[i],engajamentosList[i],
            retweetsList[i], respostasList[i], favoritosList[i], cliquesPerfilList[i])
            listaTweetsCompletos.append(tweetMontagem)

        #imprime a lista de tweets completos(teste)
        '''
        for i in listaTweetsCompletos:
            i.funcRetorno()
        '''
        self.listaTweetsCompletos = listaTweetsCompletos
    
    def maiorGenerico(self,listaTweets,termo):
        maior = listaTweets[0].funcRetornaTermo(termo)
        maiorTweet = listaTweets[0]
        for l in listaTweets:
            if(maior < l.funcRetornaTermo(termo)):
                maior = l.funcRetornaTermo(termo)
                maiorTweet = l
        return maiorTweet.funcRetorno()
        
    ''' lembrar de usar isso no menu
    maiorGenerico(listaTweetsCompletos,"engajamentos")
    maiorGenerico(listaTweetsCompletos,"impressoes")
    maiorGenerico(listaTweetsCompletos,"retweets")
    maiorGenerico(listaTweetsCompletos,"favoritos")
    '''
    ##vou ter que fazer média
    def formataHorarios(self,listaTweets):
        listaDeHorarios = []
        listaDeTweetsOrdenadaPorHorario = []
        for i in range (0,24):
            listaDeTweetsOrdenadaPorHorario.append([])
        for i in range (0,24):
            listaDeHorarios.append(0)
        #print(listaDeTweetsOrdenadaPorHorario) #so pra confirmar que foi criado uma lista de lista com os tweets ordenados por horario
        for l in listaTweets:
            vetorHorarios = l.horario.split()       #separa apenas o horario
            #print(vetorHorarios[1])
            #print(int(vetorHorarios[1][0:2]))       #numero apenas da HORA do tweet
            listaDeHorarios[int(vetorHorarios[1][0:2])] = listaDeHorarios[int(vetorHorarios[1][0:2])] + 1
            listaDeTweetsOrdenadaPorHorario[int(vetorHorarios[1][0:2])].append(l)

        return(listaDeHorarios,listaDeTweetsOrdenadaPorHorario) ## retorna uma lista com os numeros de tweets
                                                                ## e com os tweets onde em ambas listas cada indice
                                                                ## é uma hora de 0-24
    #******************************* importante

    #estruturaDeDadosHorarios = formataHorarios(listaTweetsCompletos) ##cria as duas estruturas para utilizar horarios

    #retorna o numero 3 dados
    #horario onde mais posta/numero de Tweets do mesmo/total de tweets
    def horarioComMaisTweets(self,listaDeHorarios):
        maior = listaDeHorarios[0]
        indiceHora = 0
        total = 0
        for i in range(0,len(listaDeHorarios)):
            total += i
            if listaDeHorarios[i] > maior:
                maior = listaDeHorarios[i]
                indiceHora = i   
        return(indiceHora,maior,total)  #retorna o horario/numero de Tweets do mesmo/total de tweets

    #print(horarioComMaisTweets(estruturaDeDadosHorarios[0]))  #horario que mais postou, quantas postagens, total de postagens

    #pesquisa o horario em que a media de "termo"" foi maior
    #junto com a porcentagem de "termo" nesse horario
    def horarioComMaisGenerico(self,listaDeHorarios,listaDeTweetsPorHorario,termo):
        listaDeMedias = []
        #enche a lista com elementos vazios
        for i in range (0,24):
            listaDeMedias.append(0)

        for j in range(0,24):
            numeroCalculo = 0
            for lista in listaDeTweetsPorHorario[j]:
                numeroCalculo += lista.funcRetornaTermo(termo)
            listaDeMedias[j] = numeroCalculo

        #acha o horario com mais impressoes
        maior = listaDeMedias[0]
        maiorIndice = 0
        for i in range(0,24):
            if(listaDeMedias[i] > maior):
                maior = listaDeMedias[i]
                maiorIndice = i
        return(maiorIndice, maior/sum(listaDeMedias))

    #print(horarioComMaisGenerico(estruturaDeDadosHorarios[0],estruturaDeDadosHorarios[1],"impressoes"))
    #print(horarioComMaisGenerico(estruturaDeDadosHorarios[0],estruturaDeDadosHorarios[1],"engajamentos"))

    #retorna quantos tweets possuem tal palavra
    #junto com a porcentagem de engajamento sobre os tweets com aquela palavra
    def pesquisaPorPalavras(self,listaDeTweets,palavra):
        tweetsComPalavra = 0
        impressoesPalavra = 0
        engajamentosPalavra = 0
        retweetsPalavra = 0
        respostasPalavra = 0
        favoritosPalavra = 0
        cliquesNoPerfilPalavra = 0
        
        for tweet in listaDeTweets:
            
            if search(palavra,tweet.texto,re.IGNORECASE): #se o texto contem a palavra
                tweetsComPalavra+= 1
                impressoesPalavra += tweet.impressoes
                engajamentosPalavra += tweet.engajamentos
                retweetsPalavra += tweet.retweets
                respostasPalavra += tweet.respostas
                favoritosPalavra += tweet.favoritos
                cliquesNoPerfilPalavra += tweet.cliquesNoPerfil
            
            
        return (tweetsComPalavra,
                impressoesPalavra,
                engajamentosPalavra,                             
                retweetsPalavra,
                respostasPalavra,
                favoritosPalavra,
                cliquesNoPerfilPalavra)
    #print(pesquisaPorPalavras(listaTweetsCompletos,"amigo"))


    #retorna quantos tweets possuem tal palavra
    #junto com a porcentagem de engajamento sobre os tweets com aquela palavra
    def pesquisaPorPalavrasMEDIA(self,listaDeTweets,palavra):
        tweetsComPalavra = 0
        tweetsTotal = 0
        impressoesPalavra = 0
        engajamentosPalavra = 0
        retweetsPalavra = 0
        respostasPalavra = 0
        favoritosPalavra = 0
        cliquesNoPerfilPalavra = 0
        
        impressoesTotal = 0
        engajamentosTotal = 0
        retweetsTotal = 0
        respostasTotal = 0
        favoritosTotal = 0
        cliquesNoPerfilTotal = 0
        for tweet in listaDeTweets:
            tweetsTotal += 1
            impressoesTotal += tweet.impressoes
            engajamentosTotal += tweet.engajamentos
            retweetsTotal += tweet.retweets
            respostasTotal += tweet.respostas
            favoritosTotal += tweet.favoritos
            cliquesNoPerfilTotal += tweet.cliquesNoPerfil
            if search(palavra,tweet.texto,re.IGNORECASE): #se o texto contem a palavra
                tweetsComPalavra += 1
                impressoesPalavra += tweet.impressoes
                engajamentosPalavra += tweet.engajamentos
                retweetsPalavra += tweet.retweets
                respostasPalavra += tweet.respostas
                favoritosPalavra += tweet.favoritos
                cliquesNoPerfilPalavra += tweet.cliquesNoPerfil
            
            
        return (tweetsComPalavra/tweetsTotal,
                impressoesPalavra/impressoesTotal,
                engajamentosPalavra/engajamentosTotal,                             
                retweetsPalavra/retweetsTotal,
                respostasPalavra/respostasTotal,
                favoritosPalavra/favoritosTotal,
                cliquesNoPerfilPalavra/cliquesNoPerfilTotal)
    #print(pesquisaPorPalavrasMEDIA(listaTweetsCompletos,"o"))


    def numeroTweetsPorUsuario(self,listaDeTweets,usuario):
        tweetsUsuario = 0
        for tweet in listaDeTweets:
            '''
            if usuario in tweet.texto: #se o texto contem a palavra
                tweetsUsuario += 1
            '''
            if search(usuario,tweet.texto,re.IGNORECASE):
                tweetsUsuario += 1

            '''
            if tweet.texto.find(usuario) != -1:
                tweetsUsuario = tweetsUsuario + 1
            '''
        return (tweetsUsuario)
 
    def listaUsuariosInteracaoTupla(self,listaDeTweets):
        #texto = "meu amigo @vvdc se encontrou com outro amigo @aw_moon e eu queria saber se eu @vayno consigo retirar os usuarios pelo @ mais nome deles @"
        dicionarioUsuarios = {}
        for tweet in listaDeTweets:
            texto = tweet.texto
            indiceFind = texto.find("@")
            while(indiceFind != -1):
                #print(indiceFind)
                indice = indiceFind 
                stringUsuario = ''
                while(texto[indice] != ' ' and len(texto)-1 > indice):
                    indice+=1
                    stringUsuario += texto[indice]
        
                if(len(stringUsuario) > 1):
                    #print(stringUsuario)
                    if(not stringUsuario in dicionarioUsuarios.keys()):
                        dicionarioUsuarios.update({stringUsuario:1})
                    else:
                        valor = dicionarioUsuarios.pop(stringUsuario)
                        valor += 1
                        dicionarioUsuarios.update({stringUsuario:valor})

                texto = texto[indiceFind + 1:len(texto)]
                indiceFind = texto.find("@")
        return dicionarioUsuarios
    
    def maiorInteracao(self,dicionarioUsuarios):
        listaUsuarios = list(dicionarioUsuarios.keys())
        listaValores = list(dicionarioUsuarios.values())
        maiorValor = listaValores[0]
        maiorUsuario = listaUsuarios[0]
        for i in range(0,len(listaValores)):
            if(listaValores[i] > maiorValor):
                maiorValor = listaValores[i]
                maiorUsuario = listaUsuarios[i]
        return (maiorUsuario,maiorValor)

    def formataInteracaoEngajamentoImpressoes(self,listaDeTweets):
        dicionarioFormatadoEI = {}
        for tweet in listaDeTweets:
            texto = tweet.texto
            indiceFind = texto.find("@")
            while(indiceFind != -1):
                #print(indiceFind)
                indice = indiceFind 
                stringUsuario = ''
                while(texto[indice] != ' ' and len(texto)-1 > indice):
                    indice+=1
                    stringUsuario += texto[indice]
        
                if(len(stringUsuario) > 1):
                    #print(stringUsuario)
                    if(not stringUsuario in dicionarioFormatadoEI.keys()):
                        dicionarioFormatadoEI.update({stringUsuario:(1,tweet.engajamentos,tweet.impressoes)}) #tupla(interacao,engajamentos,impressoes)
                    else:
                        valor = dicionarioFormatadoEI.pop(stringUsuario)
                        interacoes = valor[0] + 1
                        engajamentos = valor[1] + tweet.engajamentos
                        impressoes = valor[2] + tweet.impressoes
                        dicionarioFormatadoEI.update({stringUsuario:(interacoes,engajamentos,impressoes)})

                texto = texto[indiceFind + 1:len(texto)]
                indiceFind = texto.find("@")
        return dicionarioFormatadoEI
    
    def maiorInteracao_Engajamento(self,dicionario):
        listaUsuarios = list(dicionario.keys())
        listaValores = list(dicionario.values())
        maiorValor = listaValores[0][1]//listaValores[0][0] #index [i][1] engajamento
        maiorUsuario = listaUsuarios[0]
        for i in range(0,len(listaValores)):
            razao = listaValores[0][1]//listaValores[0][0]
            if(razao > maiorValor):
                maiorValor = razao
                maiorUsuario = listaUsuarios[i]
        return (maiorUsuario,maiorValor)

    def maiorInteracao_Impressao(self,dicionario):
        listaUsuarios = list(dicionario.keys())
        listaValores = list(dicionario.values())
        maiorValor = listaValores[0][2]//listaValores[0][0] #index [i][2] impressao
        maiorUsuario = listaUsuarios[0]
        for i in range(0,len(listaValores)):
            razao = listaValores[0][2]//listaValores[0][0]
            if(razao > maiorValor):
                maiorValor = razao
                maiorUsuario = listaUsuarios[i]
        return (maiorUsuario,maiorValor)