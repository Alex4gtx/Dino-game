from principal import *
import constantes as const
from random import randrange, randint


class Dino(pygame.sprite.Sprite):
    def __init__(self, spritesheet):
        pygame.sprite.Sprite.__init__(self)
        self.imagens_dinossauro = []
        for index in range(4):
            img = spritesheet.subsurface((index * 32, 0), (32, 32))
            img = pygame.transform.scale(img, (32 * 3, 32 * 3))
            self.imagens_dinossauro.append(img)

        self.indice_lista = 0
        self.image = self.imagens_dinossauro[self.indice_lista]
        self.rect = self.image.get_rect()
        self.rect.center = (100, const.ALTURA - 64)
        self.mask = pygame.mask.from_surface(self.image)
        self.pos_y_inicial = const.ALTURA - 64 - 96 // 2
        self.pulo = False

    def update(self):
        if self.pulo:
            if self.rect.y < 200:
                self.pulo = False
            self.rect.y -= 13
        else:
            if self.rect.y < self.pos_y_inicial:
                self.rect.y += 12
            else:
                self.rect.y = self.pos_y_inicial

        if self.indice_lista > 2:
            self.indice_lista = 0

        self.indice_lista += 0.15
        self.image = self.imagens_dinossauro[int(self.indice_lista)]


class Chao(pygame.sprite.Sprite):
    def __init__(self, sprite_sheet, pos_x):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((6 * 32, 0), (32, 32))
        self.image = pygame.transform.scale(self.image, (32 * 2, 32 * 2))
        self.rect = self.image.get_rect()
        self.rect.topleft = (pos_x * 61, const.ALTURA - 64)

    def update(self):
        if self.rect.topright[0] < 0:
            self.rect.x = const.LARGURA
        self.rect.x -= const.VELOCIDADE_JOGO


class Cacto(pygame.sprite.Sprite):
    def __init__(self, sprite_sheet):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 0), (32, 32))
        self.image = pygame.transform.scale(self.image, (32 * 2, 32 * 2))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.escolha = const.ESCOLHA_OBSTACULO
        self.rect.center = (const.LARGURA, const.ALTURA - 64)
        self.rect.x = const.LARGURA

    def update(self):
        if self.escolha == 0:
            if self.rect.topright[0] < 0:
                self.rect.x = const.LARGURA
            self.rect.x -= const.VELOCIDADE_JOGO


class Nuvem(pygame.sprite.Sprite):
    def __init__(self, sprite_sheet):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((7 * 32, 0), (32, 32))
        self.image = pygame.transform.scale(self.image, (32 * 3, 32 * 3))
        self.rect = self.image.get_rect()
        self.rect.y = randrange(50, 200, 50)
        self.rect.x = const.LARGURA - randrange(30, 300, 90)

    def update(self):
        if self.rect.topright[0] < 0:
            self.rect.x = randint(const.LARGURA, const.LARGURA * 2)
            self.rect.y = randrange(50, 200, 50)
        self.rect.x -= 5


class DinoVoador(pygame.sprite.Sprite):
    def __init__(self, sprite_sheet):
        pygame.sprite.Sprite.__init__(self)
        self.imagens_dinossauro = []
        for index in range(3, 5):
            img = sprite_sheet.subsurface((index * 32, 0), (32, 32))
            img = pygame.transform.scale(img, (32 * 3, 32 * 3))
            self.imagens_dinossauro.append(img)
        self.index_lista = 0
        self.image = self.imagens_dinossauro[self.index_lista]
        self.mask = pygame.mask.from_surface(self.image)
        self.escolha = const.ESCOLHA_OBSTACULO
        self.rect = self.image.get_rect()
        self.rect.center = (const.LARGURA, 300)
        self.rect.x = const.LARGURA

    def update(self):
        if self.escolha == 1:
            if self.index_lista > 1.9:
                self.index_lista = 0

            if self.rect.topright[0] < 0:
                self.rect.x = const.LARGURA

            self.rect.x -= const.VELOCIDADE_JOGO + 2
            self.index_lista += 0.15
            self.image = self.imagens_dinossauro[int(self.index_lista)]
