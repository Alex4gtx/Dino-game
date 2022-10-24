from random import choice
import os


#dimensôes de tela
LARGURA = 640
ALTURA = 480

#titulo do jogo
TITULO_JOGO = 'Dino Game'

#cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)

#fps
FPS = 60

#imagens
SPRITESHEET = 'dinoSpritesheet.png'

#musicas e sons
MUSICA_MENU = 'BoxCat Games - Victory.mp3'
SOM_PONTOS = 'score_sound.wav'
SOM_PULO = 'jump_sound.wav'
SOM_MORTE = 'death_sound.wav'

#diretórios
DIRETORIO_IMAGENS = os.path.join(os.getcwd(), 'imagens') # Diretório absoluto imagens
DIRETORIO_AUDIOS = os.path.join(os.getcwd(), 'sons') # Diretório absoluto da pasta sons

#fontes
FONTE = 'arial'

#constantes do jogo
MORTO = False
ESCOLHA_OBSTACULO = choice([0, 1])
VELOCIDADE_JOGO = 5
PONTOS = 0
MAX_PONTOS = 0
PONTOS_DELAY = 0
PONTOS_FLAG = 100
PAUSE = False
MENU = True

# COMPLEMENTOS DO HUD
ZERO = '00000'
ZERO1 = '00000'

#textos
TEXT_GOVER = 'GAME OVER'
TEXT_GOVER2 = 'Pressione R para reiniciar'
TEXT_GOVER3 = 'Press ESC para voltar ao Menu principal'

TEXT_PAUSE = 'PAUSE'
TEXT_PAUSE2 = 'Precione ESC voltar ao Menu principal'
TEXT_PAUSE3 = 'ou pressione P para voltar ao jogo'

TEXT_MENU = 'DINO GAME'
TEXT_MENU2 = 'Aperte ENTER ou SPACE para iniciar o jogo!'
TEXT_MENU3 = 'CONTROLES: SPACE = pulo e P = pause'
TEXT_MENU4 = 'Ativar/Desativar tela cheia = F'
