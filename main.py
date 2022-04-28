import pandas as pd
from classeInicial import idtextoTweet as idT #id + texto
from classeFinal import tweetCompleto as tC #tweet completo(classe com mais dados)

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
def maiorEngajamento(listaTweets):
    maior = listaTweets[0].engajamentos
    maiorTweet = listaTweets[0]
    #for i in range(0,len(listaTweets)):
    #    print(listaTweets[i].getLinkPermanente())
    for l in listaTweets:
        if(maior < l.engajamentos):
            maior = l.engajamentos
            maiorTweet = l
    return maiorTweet.funcRetorno()

##maiorEngajamento(listaTweetsCompletos)

def maiorGenerico(listaTweets,termo):
    maior = listaTweets[0].funcRetornaTermo(termo)
    maiorTweet = listaTweets[0]
    for l in listaTweets:
        if(maior < l.funcRetornaTermo(termo)):
            maior = l.funcRetornaTermo(termo)
            maiorTweet = l
    return maiorTweet.funcRetorno()
    
def maiorImpressoes(listaTweets):
    maior = listaTweets[0].impressoes
    maiorTweet = listaTweets[0]
    #for i in range(0,len(listaTweets)):
    #    print(listaTweets[i].getLinkPermanente())
    for l in listaTweets:
        if(maior < l.impressoes):
            maior = l.impressoes
            maiorTweet = l
    return maiorTweet.funcRetorno()   

maiorImpressoes(listaTweetsCompletos)