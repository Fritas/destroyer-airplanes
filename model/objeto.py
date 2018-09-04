"""

Objeto do professor Riad modificado
@author: Riad
@author: Adriano
@author: Andrei
@author: Joao
"""
from pygame import sprite

class Objeto(sprite.Sprite):
    """
    Objeto padrao para o jogo, o objeto herda da classe sprite
    """


    def __init__(self, ambiente, img, vx=0, vy=0, pos_x=0, pos_y=0):
        """
        O metodo inica um objeto padrao
        :param ambiente: ambiente pygame que o jogo esta rodando
        :param img: caminho da imagem do objeto
        :param vx: velocidade do objeto no eixo x
        :param vy: velocidade do objeto no eixo y
        :param pos_x: posicao inicial no eixo x
        :param pos_y: posicao inicial no eixo y
        """
        super().__init__()
        self.ambiente = ambiente
        self.definir_velocidade(vx, vy)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.definir_imagem(img)
        self.largura = self.ambiente.screen.get_width()
        self.altura = self.ambiente.screen.get_height()

    def definir_imagem(self, arquivo):
        """
        O metodo carrega uma imagem e a colaca objeto rect
        :param arquivo: caminho da imagem do objeto
        :return:
        """
        self.image = self.ambiente.image.load(arquivo)
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = self.pos_x
        self.rect.y = self.pos_y

    def definir_velocidade(self, velocidade_x, velocidade_y):
        """
        Cria uma lista com as velocidades do objeto
        :param velocidade_x: velocidade do objeto no eixo x
        :param velocidade_y: velocidade do objeto no eixo y
        :return:
        """
        self.velocidade = [velocidade_x, velocidade_y]

    def update(self):
        """
        Atualizar o objeto, deve ser implementado em cada objeto se necessario
        :return:
        """
        pass

    def tratar_evento(self, key=None, evento=None):
        """
        Tratar os eventos do objeto, deve ser implementado em cada objeto se necessario
        :return:
        """
        pass

    def get_image(self):
        """
        O metodo faz o get da image
        :return: a superficie da imagem
        """
        return self.image

    def get_surface(self):
        """
        O metodo faz o get da surface
        :return: a superficie contida num objeto rect
        """
        return self.rect

    def atualizar_surface(self):
        """
        O metoto atualiza a superficie
        :return:
        """
        self.rect = self.get_surface()
        self.rect.x = self.pos_x
        self.rect.y = self.pos_y

    def set_tamanho_image(self, x, y):
        """
        O metodo modifica o tamanho de uma imagem e a recoloca no rect
        :param x: o tamanho horizontal
        :param y: o tamanho vertical
        :return:
        """
        self.image = self.ambiente.transform.scale(self.image, (int(x), int(y)))
        self.rect = self.image.get_rect()  # para o retangulo ter o tamanho proporcional a image

    def transpor(self, x, y):
        """
        O metodo transpoem uma imagem
        :param x: booleano para definifir se sera transposta na horizontal
        :param y: booleano para definifir se sera transposta na vertical
        :return:
        """
        self.image = self.ambiente.transform.flip(self.image, x, y)
