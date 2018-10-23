"""
Created on 22 de jun de 2017

@author: Adriano
@author: Andrei
@author: Joao
"""
from .objeto import Objeto

class Mapa(Objeto):
    """
    A classe contem o mapa do jogo
    """

    def __init__(self, ambiente, img):
        """
        O metodo inicia um objeto mapa
        :param ambiente: ambiente pygame que o jogo esta rodando
        :param img: caminho da imagem do mapa
        """
        super().__init__(ambiente, img, 0, 0, 0, 0)
        self.set_tamanho_image(self.largura, self.altura)
