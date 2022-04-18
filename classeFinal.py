class tweetCompleto:
    def __init__(self, linkPermanente, texto, horario, impressoes, engajamentos,
  retweets, respostas, favoritos, cliquesNoPerfil 
  ):
        self.linkPermanente = linkPermanente
        self.texto = texto
        self.horario = horario
        self.impressoes = impressoes    #eh o valor de vezes que viram o tweet, porem sem relevancia com interações
        self.engajamentos = engajamentos #eh o valor de interações com o usuario
        self.retweets = retweets
        self.resposta = respostas
        self.favoritos = favoritos
        self.cliquesNoPerfil = cliquesNoPerfil

    def funcRetorno(self):
        print("Texto: ",self.texto, "\nLink permanente do Tweet: " + self.linkPermanente,
        "\nHorario: ", self.horario, "\nImpressoes: ", self.impressoes, "\nEngajamentos: ",self.engajamentos,
        "\nRetweets: ",self.retweets,"\nRespostas: ",self.resposta,"\nFavoritos: ",self.favoritos,"\nCliques no perfil: ",self.cliquesNoPerfil)