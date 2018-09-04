"""
Created on 22 de jun de 2017

@author: Adriano
@author: Andrei
@author: Joao
"""

from random import randint
from objeto_aeronave import ObjetoAeronave
from projetil import Projetil


class AeronaveNPC(ObjetoAeronave):


    def __init__(self, ambiente, img_aeronave, img_projetil, dano, resistencia, vida, velocidade_tiro, velocidade):
        """
        O metodo inicia um objeto aeronave npc

        :param ambiente: ambiente pygame que o jogo esta rodando
        :param img_aeronave: caminho da imagem da aeronave
        :param img_projetil: caminho da imagem do projetil
        :param dano: valor numerico do dano
        :param resistencia: valor numerico da resistencia
        :param vida: valor numerico da vida
        :param velocidade_tiro: valor numerico da velocidade do tiro
        :param velocidade: tupla com as velocidades da nave (velocidade_x, velocidade_y)
        """
        super().__init__(ambiente, img_aeronave, img_projetil, dano, resistencia, vida, velocidade_tiro, velocidade)
        self.set_tamanho_image((self.largura * 0.10), (self.altura * 0.10))
        self.definir_coord()
        self.transpor(False, True)

    def update(self):
        """
        O metodo atualiza o NPC
        :return:
        """
        self.pos_y += self.velocidade[1]
        self.atualizar_surface()
        self.grup_tiros.update()

    def atirar(self):
        """
        Gera o tiro do NPC
        :return:
        """
        pos_x_projetil = self.pos_x + self.image.get_width() / 2
        pos_y_projetil = self.pos_y + self.image.get_height() - 20
        projetil = Projetil(self.ambiente, (pos_x_projetil, pos_y_projetil), self.dano, (self.velocidade_tiro), self.img_projetil)
        projetil.transpor(False, True)
        self.grup_tiros.add(projetil)

    def status_posicao(self):
        """
        O metodo verifica se a aeronave ainda esta no mapa\
         ou nos extremos do mapa permitido
        :return:True se estiver, False se nao estiver
        """
        if self.pos_x > self.largura or self.pos_y > self.altura or self.pos_x < 0:
            return False
        return True

    def definir_coord(self):
        """
        O metodo define as posicoes x e y inicias do NPC
        :return:
        """
        self.pos_x = randint(0, (self.largura -  self.image.get_width()))
        self.pos_y -= self.image.get_height() #para ele comecar antes do mapa e ir entrando no mapa
