"""
Created on 29 de jun de 2017

@author: Adriano
@author: Andrei
@author: Joao
"""

from objeto_aeronave import ObjetoAeronave
from projetil import Projetil

class AeronaveJogador(ObjetoAeronave):
    """
    O objeto eh a aeronave do jogador
    """


    def __init__(self, ambiente, img_aeronave, img_projetil, dano, resistencia, vida, combustivel, velocidade_tiro, velocidade):
        """
        O metodo inicia um objeto aeronave jogador

        :param ambiente: ambiente pygame que o jogo esta rodando
        :param img_aeronave: caminho da imagem da aeronave
        :param img_projetil: caminho da imagem do projetil
        :param dano: valor numerico do dano
        :param resistencia: valor numerico da resistencia
        :param vida: valor numerico da vida
        :param combustivel: valor numerico da quantidade inicial do combustivel da aeronave do jogador
        :param velocidade_tiro: valor numerico da velocidade do tiro
        :param velocidade: tupla com as velocidades da nave (velocidade_x, velocidade_y)
        :param pos_x: posicao x inicial no mapa
        :param pos_y: posicao y inicial no mapa
        """
        super().__init__(ambiente, img_aeronave, img_projetil, dano, resistencia, vida, velocidade_tiro, velocidade)
        self.set_tamanho_image((self.largura * 0.10), (self.altura * 0.10))
        self.definir_coord()
        self.combustivel = combustivel
        self.inicializar_som()
        self.definir_teclas()

    def definir_teclas(self):
        """
        O metodo defini as teclas da aeronave
        :return:
        """
        self.esquerda = self.ambiente.K_LEFT
        self.direita = self.ambiente.K_RIGHT
        self.cima = self.ambiente.K_UP
        self.atirar_espaco = self.ambiente.K_SPACE

    def inicializar_som(self):
        """
        Crias as variveis do sons da aeronave
        :return:
        """
        self.som_tiro = self.ambiente.mixer.Sound('static/sound/tiro.wav')
        self.som_tiro.set_volume(0.5)

    def definir_coord(self):
        """
        Defini como devem ser as coordenadas inicias da aeronave do jogador
        :return:
        """
        self.pos_y = self.altura - self.altura * 0.20
        self.pos_x = self.largura // 2

    def atirar(self):
        """
        Gera o tiro do jogador
        :return:
        """
        if self.ambiente.som_effects:
            self.som_tiro.play()
        pos_x_projetil = self.pos_x + self.image.get_width() / 2
        self.grup_tiros.add(Projetil(self.ambiente, (pos_x_projetil, self.pos_y), self.dano, (-self.velocidade_tiro), self.img_projetil))

    def update(self):
        """
        Atualizacao da aeronave a cada loop
        :return:
        """
        self.atualizar_surface()
        self.grup_tiros.update()

    def tratar_eventos(self, key=None):
        """
        Trata dos eventos da aeronave jogador
        :param key: teclas pressionadas numa variavel resultante do comando 'self.ambiente.key.get_pressed()'
        :return:
        """
        if key[self.esquerda]:
            self.pos_x -= self.velocidade[0]
            if self.pos_x < 0:
                self.pos_x += self.velocidade[0]
        elif key[self.direita]:
            self.pos_x += self.velocidade[0]
            if (self.pos_x + self.image.get_width()) > self.largura:
                self.pos_x -= self.velocidade[0]
        if key[self.cima] or key[self.atirar_espaco]:
            if self.ambiente.time_tiro >= 160:
                self.atirar()
                self.ambiente.time_tiro = 0

    def status(self):
        """
        verifica se a aeronave ainda esta viva e se tem combustivel
        :return: se esta estiver viva e com combustivel retorna True, se não retorna False
        """
        if self.combustivel > 0 and self.vida > 0:
            return True
        return False

    def adicionar_drop(self, drop):
        """
        Recebe um objeto drop e atribui seu beneficio a aeronave
        :param drop: um objeto do tipo drop
        :return:
        """
        if drop.modelo == 'vida':
            self.vida += drop.incrementacao
            if self.vida > 100:
                self.vida = 100
        elif drop.modelo == 'combustivel':
            self.combustivel += drop.incrementacao
            if self.combustivel > 100:
                self.combustivel = 100
        elif drop.modelo == 'dano_extra':
            pass
        elif drop.modelo == 'resistencia_extra':
            pass
