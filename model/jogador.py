"""
Created on 29 de jun de 2017

@author: Adriano
@author: Andrei
@author: Joao
"""
from .aeronave_jogador import AeronaveJogador

class Jogador(object):
    """
    A classe contem um jogador
    """

    pontos = 0

    def __init__(self, ambiente, nome, img_aeronave=None):
        """
        o metodo inicia um objeto jogador
        :param ambiente: ambiente pygame que o jogo esta rodando
        :param nome: string com o nome do jogador
        :param img_aeronave: caminho da imagem da aeronave
        """
        self.ambiente = ambiente
        self.nome = nome
        self.adicionar_aeronave(img_aeronave)

    def adicionar_aeronave(self, img_aeronave):
        """
        O metodo cria um objeto aeronave para o jogador
        :param img_aeronave: caminho da imagem da aeronave
        :return:
        """
        try:
            self.aeronave = AeronaveJogador(self.ambiente, img_aeronave, 'static/img/projetil/projetil.gif',
                                       6, 3, 100, 100, 15, (10, 0))
        except self.ambiente.error:
            self.aeronave = AeronaveJogador(self.ambiente, 'static/img/aeronave/aviaoJogador.gif', 'static/img/projetil/projetil.gif',
                                       6, 3, 100, 100, 15, (10, 0))
