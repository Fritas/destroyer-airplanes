"""
Created on jun de 2017

@author: Adriano
@author: Andrei
@author: Joao
"""
from random import randint
from objeto import Objeto



class ObjetoDrop(Objeto): #RS(001, 002, 003, 004, 005)

    def __init__(self, ambiente, img, modelo):
        """
        O metodo inicia um objeto drop

        :param ambiente: ambiente pygame que o jogo esta rodando
        :param img: caminho da imagem do drop
        :param modelo: string com letras em minusculo sem acento escrito o tipo do drop
        """

        Objeto.__init__(self, ambiente, img, 0, 2, 0, 0)
        self.modelo = modelo
        self.set_tamanho_image((self.largura * 0.05), (self.altura * 0.05))
        self.pos_y -= self.image.get_height()
        self.pos_x = randint(0, self.largura)
        self.definir_incrementacao()

    def definir_incrementacao(self):
        """
        O metodo sorteia um numero de 0 a 100 para definir quando de incrementacao o \
        drop vai dar quando o jogador sofrer colisao com ele
        :return:
        """
        self.incrementacao = randint(0, 100)

    def update(self):
        """
        O metodo atualiza o objeto
        :return:
        """
        self.pos_y += self.velocidade[1]
        self.atualizar_surface()


    def status_posicao(self):
        """
        O metodo verifica se a drop ainda esta no mapa
        :return: True se estiver, False se nao estiver
        """
        if self.pos_x > self.largura or self.pos_y > self.altura or self.pos_x < 0:
            return False
        return True
