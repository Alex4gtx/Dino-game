import pygame, os, sprites_classes
import constantes as const
from sys import exit
from random import choice


class Jogo:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.tela = pygame.display.set_mode((const.LARGURA, const.ALTURA))
        pygame.display.set_caption(const.TITULO_JOGO)
        self.relogio = pygame.time.Clock()
        self.fonte = pygame.font.match_font(const.FONTE)
        self.esta_rodando = True
        self.carregar_arqivos()
    
    def carregar_arqivos(self):
        """Carrega os arquivos de imagem e som através de diretórios"""
        self.spritesheet = pygame.image.load(os.path.join(const.DIRETORIO_IMAGENS, const.SPRITESHEET)).convert_alpha() #spritesheet carregada
        self.som_pontos = pygame.mixer.Sound(os.path.join(const.DIRETORIO_AUDIOS, const.SOM_PONTOS)) #som emitido a cada 100pts
        self.som_pulo = pygame.mixer.Sound(os.path.join(const.DIRETORIO_AUDIOS, const.SOM_PULO)) # som dos pulos
        self.som_colisao = pygame.mixer.Sound(os.path.join(const.DIRETORIO_AUDIOS, const.SOM_MORTE)) #som emitido quando morre
        
    def eventos_principais(self):
        """Define os eventos do jogo"""
        #eventos do teclado
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                self.esta_rodando = False
                exit()

            # ação de pular
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if self.dino.rect.y != self.dino.pos_y_inicial:
                        pass
                    else:
                        self.dino.pulo = True
                        self.som_pulo.play()
                    
                if event.key == pygame.K_p:
                    const.PAUSE = True
                        
        #eventos do jogo
        self.evento_colisao()

        #logica de escolha cacto x dino voador
        if self.dino_voador.rect.topright[0] <= 0 or self.cacto.rect.topright[0] <= 0:
            const.ESCOLHA_OBSTACULO = choice([0, 1])
            self.cacto.rect.x, self.dino_voador.rect.x = const.LARGURA, const.LARGURA
            self.cacto.escolha, self.dino_voador.escolha = const.ESCOLHA_OBSTACULO, const.ESCOLHA_OBSTACULO
        
        # sistema de pontuação
        const.PONTOS_DELAY += 0.4
        if const.PONTOS_DELAY >= 1:
            const.PONTOS_DELAY = 0
            const.PONTOS += 1

        # som que toca de 100 em 100 pts
        if const.PONTOS == const.PONTOS_FLAG:
            self.som_pontos.play()
            if const.VELOCIDADE_JOGO >= 14:
                pass
            else:
                const.VELOCIDADE_JOGO += 0.7
            const.PONTOS_FLAG += 100
    
    def evento_colisao(self):
        """eventos apenas de ações de colisão"""
        self.colisoes = pygame.sprite.spritecollide(self.dino, self.grupo_obstaculo, False, pygame.sprite.collide_mask)
        
        if self.colisoes:
            self.som_colisao.play()
            if const.PONTOS > const.MAX_PONTOS:
                const.MAX_PONTOS = const.PONTOS
            const.MORTO = True
            self.jogando = False

    def reiniciar_jogo(self):
        self.dino.rect.y = self.dino.pos_y_inicial
        self.grupo_obstaculo.remove(self.dino)
        self.dino_voador.rect.x = const.LARGURA
        self.cacto.rect.x = const.LARGURA
        const.ESCOLHA_OBSTACULO = choice([0, 1])
        self.dino.pulo = False
        const.PONTOS = 0
        const.VELOCIDADE_JOGO = 5
        const.MORTO = False
        const.ZERO = '00000'
        const.MENU = False
        self.jogando = True

    def mostrar_texto(self, texto, tamanho, cor, x, y):
        """Função que mostra texto"""
        fonte = pygame.font.Font(self.fonte, tamanho)
        texto = fonte.render(texto, True, cor)
        texto_rect = texto.get_rect()
        texto_rect.midtop = (x, y)
        self.tela.blit(texto, texto_rect)
    
    def novo_jogo(self):
        """Instancia as classes de sprites do jogo"""

        # grupos de sprites
        self.todas_as_sprites = pygame.sprite.Group() #grupo com todas as sprites
        self.grupo_obstaculo = pygame.sprite.Group() #grupo com as sprites considerados obstaculos

        # sprite dino
        self.dino = sprites_classes.Dino(self.spritesheet)
        self.todas_as_sprites.add(self.dino)

        # sprite chão
        for i in range(const.LARGURA * 2 // 64):
            self.chao = sprites_classes.Chao(self.spritesheet, i)
            self.todas_as_sprites.add(self.chao)

        # sprite cacto
        self.cacto = sprites_classes.Cacto(self.spritesheet)
        self.todas_as_sprites.add(self.cacto)

        # sprites nuvens
        for i in range(3):
            self.nuvem = sprites_classes.Nuvem(self.spritesheet)
            self.todas_as_sprites.add(self.nuvem)
        
        # sprite dino voador
        self.dino_voador = sprites_classes.DinoVoador(self.spritesheet)
        self.todas_as_sprites.add(self.dino_voador)

        # add os obstaculos
        self.grupo_obstaculo.add(self.dino_voador)
        self.grupo_obstaculo.add(self.cacto)

        self.rodar()
    
    def hud(self):
        """HUD principal do jogo"""
        # textos de pontuação
        self.mostrar_texto(f'Pontos: {const.ZERO}{const.PONTOS}', 25, const.PRETO, 550, 0)
        self.mostrar_texto(f'Maior pontuação: {const.ZERO1}{const.MAX_PONTOS}', 25, const.PRETO, 350, 0)

        # adiciona zeros na frente da pontuação
        if const.PONTOS == 10:
            const.ZERO = '0000'
        elif const.PONTOS == 100:
            const.ZERO = '000'
        elif const.PONTOS == 1000:
            const.ZERO = '00'
        elif const.PONTOS == 10000:
            const.ZERO = '0'
        elif const.PONTOS >= 100000:
            const.ZERO = ''

        if 10 <= const.MAX_PONTOS < 100:
            const.ZERO1 = '0000'
        elif 100 <= const.MAX_PONTOS < 1000:
            const.ZERO1 = '000'
        elif 1000 <= const.MAX_PONTOS < 10000:
            const.ZERO1 = '00'
        elif 10000 <= const.MAX_PONTOS < 100000:
            const.ZERO1 = '0'
        elif const.MAX_PONTOS >= 100000:
            const.ZERO1 = ''

    def rodar(self):
        """Loop de jogo"""
        pygame.mixer.music.stop()
        self.jogando = True
        while self.jogando:
            self.relogio.tick(const.FPS)
            self.eventos_principais()
            self.pause()
            self.desenhar_sprites()
            self.atualizar_sprites()
    
    def desenhar_sprites(self):
        """Desenha todas as sprites na tela"""
        self.tela.fill(const.BRANCO)
        self.todas_as_sprites.draw(self.tela)
        self.hud()
        pygame.display.flip()
    
    def atualizar_sprites(self):
        """Atualiza sprites"""
        self.todas_as_sprites.update()
    
    def mostrar_tela_start(self):
        if const.MENU:
            pygame.mixer.music.load(os.path.join(const.DIRETORIO_AUDIOS, const.MUSICA_MENU))
            pygame.mixer.music.set_volume(1)
            pygame.mixer.music.play(-1)
        while const.MENU:
            self.relogio.tick(const.FPS)
            self.tela.fill(const.BRANCO)
            self.mostrar_texto(const.TEXT_MENU, 80, const.PRETO, const.LARGURA/2, 50)
            self.mostrar_texto(const.TEXT_MENU2, 20, const.PRETO, const.LARGURA/2, 130)
            self.mostrar_texto(const.TEXT_MENU3, 20, const.PRETO, const.LARGURA/2, const.ALTURA - 60)
            self.mostrar_texto(const.TEXT_MENU4, 20, const.PRETO, const.LARGURA/2, const.ALTURA - 30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.esta_rodando = False
                    pygame.quit()
                    exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE or event.key == pygame.K_KP_ENTER:
                        const.MENU = False
                    
                    if event.key == pygame.K_f:
                        pygame.display.toggle_fullscreen()
        
            pygame.display.flip()
    
    def game_over(self):
        """Tela de game over"""
        while const.MORTO:
            self.relogio.tick(const.FPS)
            #eventos do teclado
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.esta_rodando = False
                    exit()
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.reiniciar_jogo()
                    
                    if event.key == pygame.K_ESCAPE:
                        self.reiniciar_jogo()
                        const.MENU = True

            # TEXTOS E POSIÇÕES DA UI
            posx, posy = const.LARGURA/2, const.ALTURA/2 - 25
            self.mostrar_texto(const.TEXT_GOVER, 50, const.PRETO, posx, posy)
            posy += 45
            self.mostrar_texto(const.TEXT_GOVER2, 25, const.PRETO, posx, posy)
            posy += 25
            self.mostrar_texto(const.TEXT_GOVER3, 25, const.PRETO, posx, posy)
            pygame.display.flip()

    def pause(self):
        while const.PAUSE:
            self.relogio.tick(const.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.esta_rodando = False
                    exit()
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        const.PAUSE = False
                    
                    if event.key == pygame.K_ESCAPE:
                        self.reiniciar_jogo()
                        const.MENU = True
                        const.PAUSE = False
                        self.jogando = False
            
            posx, posy = const.LARGURA/2, const.ALTURA/2
            self.mostrar_texto(const.TEXT_PAUSE, 50, const.PRETO, posx, posy)
            posy += 50
            self.mostrar_texto(const.TEXT_PAUSE2, 25, const.PRETO, posx, posy)
            posy += 25
            self.mostrar_texto(const.TEXT_PAUSE3, 25, const.PRETO, posx, posy)

            pygame.display.flip()
                
                
game = Jogo() #instancia da classe principal

while game.esta_rodando:
    game.mostrar_tela_start()
    game.novo_jogo()
    game.game_over()
