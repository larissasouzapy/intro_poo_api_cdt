'''
Objeto:uma pasta onde tem varios arquivos que podem ser moldados e dão caracteristicas e ações a pasta
winx - Flora
MonsterHight - Draculaura
My Little Pony - Pinkpie
'''



class BonecoToyStory:

    def __init__(self, nome, dono, frase_de_efeito):
        self.nome = nome
        self.dono = dono 
        self.frase_de_efeito = frase_de_efeito



woody = BonecoToyStory(
   nome = "Woody",
   dono = "Andy",
   frase_de_efeito = "Há uma cobra na minha bota!",
)

jassie = BonecoToyStory(
    nome = "Jessie",
    dono = "Emily",
    frase_de_efeito = "Quando alguém me ama, tudo era hermoso",
)

betty = BonecoToyStory(
    nome = "Betty",
    dono = "Molly Davis",
    frasse_de_efeito = "As brincadeiras acabaram!",
)