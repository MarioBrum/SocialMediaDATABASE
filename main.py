import pandas as pd

tabela = pd.read_csv('tweet_activity_metrics_vayno_20220312_20220409_pt.csv')
print(tabela)
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
print(tabela)