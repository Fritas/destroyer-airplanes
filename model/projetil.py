"""
Created on 3 de jul de 2017

@author: Adriano
@author: Andrei
@author: Joao
"""

from random import randint
from objeto import Objeto


class Projetil(Objeto):


    def __init__(self, ambiente, posicao, dano, velocidade, img):
        """
        O metodo inicia o objeto projetil

        :param ambiente: ambiente pygame que o jogo esta rodando
        :param posicao: tupla com as posicoes x e y da aeronave (pos_x, pos_y)
        :param dano: valor do dano da aeronave
        :param velocidade: velocidade do projetil valor int
        :param img: caminho da imagem do projetil
        """
        pos_x, pos_y = posicao
        super().__init__(ambiente, img, 0, velocidade, pos_x, pos_y)
        self.definir_dano(dano)
        self.pos_x -= self.image.get_width() / 2
        self.atualizar_surface()

    def definir_dano(self, dano):
        """
        O metodo sortei um valor de 1 ate o valor de dano para o dano que\
        sera efetuado caso o projetil acerte outra aeronave
        :param dano: valor do dano da aeronave
        :return:
        """
        self.dano = randint(1, dano)

    def update(self):
        """
        O metodo atualiza o projetil
        :return:
        """
        self.pos_y += self.velocidade[1]
        self.atualizar_surface()
