"""
Created on jun de 2017

@author: Adriano
@author: Andrei
@author: Joao
"""
from .objeto import Objeto

class ObjetoAeronave(Objeto):
    """
        Objeto base para aeronaves do jogo
    """

    def __init__(self, ambiente, img_aeronave, img_projetil, dano, resistencia, vida, velocidade_tiro, velocidade, pos_x=0, pos_y=0):
        """
        O metodo inicia um objeto aeronave

        :param ambiente: ambiente pygame que o jogo esta rodando
        :param img_aeronave: caminho da imagem da aeronave
        :param img_projetil: caminho da imagem do projetil
        :param dano: valor numerico do dano
        :param resistencia: valor numerico da resistencia
        :param vida: valor numerico da vida
        :param velocidade_tiro: valor numerico da velocidade do tiro
        :param velocidade: tupla com as velocidades da nave (velocidade_x, velocidade_y)
        :param pos_x: posicao x inicial no mapa
        :param pos_y: posicao y inicial no mapa
        """
        super().__init__(ambiente, img_aeronave, velocidade[0], velocidade[1], pos_x, pos_y)
        self.definir_velocidade_tiro(velocidade_tiro)
        self.dano = dano
        self.resistencia = resistencia
        self.vida = vida
        self.img_projetil = img_projetil
        self.grup_tiros = self.ambiente.sprite.Group()

    def definir_velocidade_tiro(self, velocidade):
        """
        O metodo define velocidade como um numero inteiro
        :param velocidade:
        :return: None
        """
        self.velocidade_tiro = int(velocidade)

    def update(self):
        """
        Metodo que deve ser reimplementado em toda aeronave para definir as atualizaoes dela a cada loop do jogo
        :return:
        """
        pass

    def tratar_evento(self, key=None, evento=None):
        """
        Metodo que deve ser reimplementado em toda aeronave para definir os comportamentos
        :param key:
        :param evento:
        :return:
        """
        pass

    def status_vida(self):
        """
        verifica se a aeronave ainda esta viva
        :return: se esta vivo retorna True, se estiver morto retorna False
        """
        if self.vida > 0:
            return True
        return False

    def atirar(self):
        """
        Metodo que deve ser reimplementado  com o tiro da aeronave
        :return:
        """
        pass
