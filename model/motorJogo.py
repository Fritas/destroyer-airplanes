"""
Created on jun de 2017

@author: Adriano
@author: Andrei
@author: Joao
"""
from random import randint
from .mapa import Mapa
from .objeto_drop import ObjetoDrop
from .jogador import Jogador
from .aeronave_npc import AeronaveNPC


class Jogo(object):
    """
    A classe jogo gerencia o motor do jogo
    """

    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    screen = None
    profundidade_das_cores = 32
    lista_grups = []
    lista_jogadores = []
    lista_caixa_de_texto = []
    cont = 0
    clock_tick = 30

    def __init__(self, ambiente, titulo_da_tela, dimensoes_da_tela, jogadores=None, profundidade_das_cores=32,  flag=None):
        """
        O metodo inicia o motor do jogo

        :param ambiente: ambiente pygame que o jogo sera rodado
        :param titulo_da_tela: string com o texto a ser exibido na barra da janela
        :param dimensoes_da_tela: tupla com o tamanho da tela (tamanho_x, tamanho_y)
        :param jogadores: lista com objetos jogadores
        :param profundidade_das_cores: numero de pixel das cores
        :param flag: tipo de exibicao que o jogo tera
        """
        self.ambiente = ambiente
        self.ambiente.mixer.init()
        self.ambiente.init()
        print(self.ambiente.get_error())

        self.dimensao = self.largura, self.altura = dimensoes_da_tela
        self.flag = flag
        self.profundidade_das_cores = profundidade_das_cores
        self.titulo_da_tela = titulo_da_tela
        self.fonte = self.ambiente.font.Font(None, 25)
        self.inicializar_screen()
        self.inicializar_som()
        self.carregar_jogadores(jogadores)

        #grups
        self.grup_cenario = self.ambiente.sprite.Group()
        self.grup_jogador_aeronave = self.ambiente.sprite.Group()
        self.grup_tiros_jogador = self.ambiente.sprite.Group()
        self.grup_npc = self.ambiente.sprite.Group()
        self.grup_drops = self.ambiente.sprite.Group()
        #add grups
        self.lista_grups.append(self.grup_cenario)
        self.lista_grups.append(self.grup_jogador_aeronave)
        self.lista_grups.append(self.grup_tiros_jogador)
        self.lista_grups.append(self.grup_npc)
        self.lista_grups.append(self.grup_drops)

    ######################### INICIALIZAR #########################
    def inicializar_screen(self):
        """
        O metodo cria o display do jogo e adiciona no ambiente
        :return:
        """
        self.ambiente.display.set_caption(self.titulo_da_tela)
        self.ambiente.screen = self.ambiente.display.set_mode(self.dimensao, self.flag, self.profundidade_das_cores)

    def inicializar_cenario(self, img_mapa):
        """
        O metodo inicia os objetos do cenario do jogo
        :param img_mapa: caminho da imagem do mapa
        :return:
        """
        try:
            self.grup_cenario.add(Mapa(self.ambiente, img_mapa))
        except self.ambiente.error:
            self.grup_cenario.add(Mapa(self.ambiente, 'static/img/mapa/mapa3.jpg'))

    def inicializar_som(self):
        """
        O metodo salva as variaveis com os respectivos objetos referentes aos seus sons
        :return:
        """
        self.ambiente.som_effects = True
        self.som_destruicao_npc = self.ambiente.mixer.Sound('static/sound/destruicao_npc.wav')
        self.som_destruicao_npc.set_volume(1)
        self.som_derrota = self.ambiente.mixer.Sound('static/sound/derrota.wav')

    ######################### ADICIONAR #########################
    def carregar_jogadores(self, jogadores):
        """
        O metodo carrega os jogadores da lista jogadores
        :param jogadores: lista dos jogadores
        :return:
        """
        for jogador in jogadores:
            self.lista_jogadores.append(jogador)
            jogador.pontos = 0
            self.grup_jogador_aeronave.add(jogador.aeronave)

    def adicionar_jogador(self, nome, img_aeronave=None):
        """
        O metodo adiciona um jogador
        :param nome: string com o nome do jogador
        :param img_aeronave: caminho da imagem da aeronave do jogador
        :return:
        """
        jogador = Jogador(self.ambiente, nome, img_aeronave)
        self.lista_jogadores.append(jogador)
        self.grup_jogador_aeronave.add(jogador.aeronave)

    def adicionar_drop_npc(self):
        """
        Adiciona npc e drop periodicamento quando o jogo esta rodando
        :return:
        """
        if self.cont % 10 == 0:
            for jogador in self.lista_jogadores:
                jogador.aeronave.combustivel -= 0.1
                jogador.aeronave.combustivel = round(jogador.aeronave.combustivel, 1)

        if self.cont % 120 == 0:
            self.criar_npc()

        if self.cont % 150 == 0:
            self.criar_drop()

    def criar_npc(self):
        """
        o metodo cria um objeto aeronaveNPC
        :return:
        """
        if randint(0, 1):
            aeronave = AeronaveNPC(self.ambiente, 'static/img/aeronave/aviaoNPC.gif', 'static/img/projetil/projetil.gif', 6, 2, 100, 15, (0, 3))
        else:
            aeronave = AeronaveNPC(self.ambiente, 'static/img/aeronave/helicopteroNPC.gif', 'static/img/projetil/projetil.gif', 6, 4, 50, 15, (0, 3))
        self.grup_npc.add(aeronave)

    def criar_drop(self):
        """
        O metodo cria um objeto drop
        :return:
        """
        opcao = randint(0, 1)

        if opcao == 0:
            self.grup_drops.add(ObjetoDrop(self.ambiente, 'static/img/drop/vida.gif', 'vida'))
        elif opcao == 1:
            self.grup_drops.add(ObjetoDrop(self.ambiente, 'static/img/drop/combustivel.gif', 'combustivel'))
        elif opcao == 2:
            self.grup_drops.add(ObjetoDrop(self.ambiente,'static/img/drop/resistencia_extra.gif', 'resistencia_extra'))
        elif opcao == 3:
            self.grup_drops.add(ObjetoDrop(self.ambiente, 'static/img/drop/dano_extra.gif', 'dano_extra'))

    def criar_caixa_de_texto(self, texto, font_size, pos_x, pos_y):
        """
        O metodo cria um objeto aeronaveNPC
        :param texto: string com o texto
        :param font_size: tamanho da fonte
        :param pos_x: posicao x de onde o texto deve aparecer
        :param pos_y: posicao y de onde o texto deve aparecer
        :return:
        """
        fonte = self.ambiente.font.Font(None, font_size)
        text = fonte.render(texto, True, self.WHITE)
        rect = text.get_rect()
        distancia_x, distancia_y = text.get_size()
        rect = rect.move((pos_x - distancia_x, (pos_y - distancia_y)))
        self.ambiente.screen.blit(text, rect)

    ######################### ATUALIZAR #########################
    def atualizar_objetos(self):
        """
        O metodo atualiza todos os objetos da tela
        :return:
        """
        for grup in self.lista_grups:
            grup.update()

        for jogador in self.lista_jogadores:
            self.atualizar_jogador(jogador)
            for npc in self.grup_npc:
                #atualizando npc
                self.atualiar_npc(npc)
                #atualizando npc com aeronave
                self.atualizar_aeronave_npc(jogador, npc)
                #atualizando drop
                for drop in self.grup_drops:
                    self.atualizar_drop(drop)

    def atualiar_npc(self, npc):
        """
        O metodo atualiza as questoes relacionadas a um npc
        :param npc: objeto aeronaveNPC a ser atualizado
        :return:
        """
        #colisao npc com drop
        self.ambiente.sprite.groupcollide(self.grup_npc, self.grup_drops, False, True, None)
        #colisao tiro npc com drops
        self.ambiente.sprite.groupcollide(npc.grup_tiros, self.grup_drops, True, True, None)
        #colisao tiro npc com npc
        grup_npc = self.grup_npc.copy()
        grup_npc.remove(npc)
        self.ambiente.sprite.groupcollide(npc.grup_tiros, grup_npc, True, False)
        #atualizar npc
        if not npc.status_posicao():
            self.grup_npc.remove(npc)
        if self.cont % 8 == 0:
            npc.atirar()
            npc.grup_tiros.update()

    def atualizar_jogador(self, jogador):
        """
        O objeto atualiza as questoes relacionadas a um jogador
        :param jogador: objeto jogador a ser atualizado
        :return:
        """
        aeronave = jogador.aeronave
        #colisao tiros aeronave com drop
        self.ambiente.sprite.groupcollide(aeronave.grup_tiros, self.grup_drops, True, True, None)
        #colisao aeronave com drop
        drop = self.ambiente.sprite.spritecollideany(aeronave, self.grup_drops, collided=None)
        if drop:
            aeronave.adicionar_drop(drop)
            self.grup_drops.remove(drop)

    def atualizar_aeronave_npc(self, jogador, npc):
        """
        O metodo atualiza as questoes relacionadas entre um jogador e um npc
        :param jogador: objeto Jogador
        :param npc: objeto aeronaveNPC
        :return:
        """
        aeronave = jogador.aeronave
        #colisao tiros npc com tiros aeronave
        self.ambiente.sprite.groupcollide(aeronave.grup_tiros, npc.grup_tiros, True, True, None)
        #tiro aeronave com o npc
        projetil = self.ambiente.sprite.spritecollideany(npc, aeronave.grup_tiros, collided=None)
        if projetil:
            if projetil.dano > npc.resistencia:
                npc.vida -= projetil.dano
            jogador.pontos += projetil.dano * 2
            if not npc.status_vida():
                self.som_destruicao_npc.play()
                self.grup_npc.remove(npc)
                jogador.pontos += 20
            aeronave.grup_tiros.remove(projetil)
        #colisao tiro npc com aeronave
        projetil = self.ambiente.sprite.spritecollideany(aeronave, npc.grup_tiros, collided=None)
        if projetil:
            if projetil.dano > aeronave.resistencia:
                aeronave.vida -= projetil.dano
                jogador.pontos -= projetil.dano
            if jogador.pontos < 0:
                jogador.pontos = 0
            if not aeronave.status_vida():
                self.grup_jogador_aeronave.remove(aeronave)
            npc.grup_tiros.remove(projetil)
        #colisao npc com aeronave
        batida = self.ambiente.sprite.collide_rect(aeronave, npc)
        if batida:
            aeronave.vida -= batida
            npc.vida -= batida

    def atualizar_drop(self, drop):
        """
        O metodo atualiza um drop
        :param drop: Objeto drop
        :return:
        """
        if not drop.status_posicao():
            self.grup_drops.remove(drop)

    def atualizar_tela(self):
        """
        O metodo atualiza a tela do jogo
        :return:
        """
        self.ambiente.display.flip()
        for grup in self.lista_grups:
            grup.draw(self.ambiente.screen)  # desenha todos os objetos na tela

        for jogador in self.lista_jogadores:
            jogador.aeronave.grup_tiros.draw(self.ambiente.screen)
            self.atualizar_caixa_de_texto(jogador)

        for npc in self.grup_npc:
            npc.grup_tiros.draw(self.ambiente.screen)

    def atualizar_caixa_de_texto(self, jogador):
        """
        O metodo atualiza a caixa de texto com as informacoes do jogador
        :param jogador: objeto Jogador
        :return:
        """
        texto_da_superficie = str(jogador.nome) + ' >  ' \
                              + 'Vida: ' + str(jogador.aeronave.vida) + '  ' \
                              + 'Combustivel: ' + str(jogador.aeronave.combustivel) + '  ' \
                              + 'Pontos: ' + str(jogador.pontos)

        text = self.fonte.render(texto_da_superficie, True, self.WHITE)
        rect = text.get_rect()
        distancia_x, distancia_y = text.get_size()
        rect = rect.move((self.largura - distancia_x - 20), (self.altura - distancia_y * 2))
        self.ambiente.screen.blit(text, rect)

    ######################### JOGANDO #########################
    def ligar_desligar_som(self):
        """
        O metodo liga e desliga os efeitos sonoros do jogo
        :return:
        """
        self.ambiente.som_effects = not self.ambiente.som_effects
        if self.ambiente.som_effects:
            self.criar_caixa_de_texto('Som: ligado', 30, self.largura / 2, self.altura / 2)
        else:
            self.criar_caixa_de_texto('Som: Desligado', 30, self.largura / 2, self.altura / 2)

    def status_jogo(self):
        """
        O jogo verifica se existe um jogador habito a jogar ainda
        :return: True se exister, False se nao existir
        """
        for jogador in self.lista_jogadores:
            if not jogador.aeronave.status():
                self.grup_jogador_aeronave.remove(jogador.aeronave)
                self.lista_jogadores.remove(jogador)
        if self.lista_jogadores:
            return True
        return False

    def tratar_eventos(self):
        """
        O metodo trata os eventos do jogo
        :return:
        """
        for evento in self.ambiente.event.get():
            key = self.ambiente.key.get_pressed()
            if evento.type == self.ambiente.QUIT or key[self.ambiente.K_ESCAPE]:
                print("Quit!")
                return False
            if key[self.ambiente.K_s]:
                self.ligar_desligar_som()
            for jogador in self.lista_jogadores:
                jogador.aeronave.tratar_eventos(key)
        return True

    def iniciar_jogo(self, img_mapa=None):
        """
        O metodo inicia o jogo
        :param img_mapa: caminho da imagem do mapa
        :return:
        """
        jogar = True
        self.ambiente.key.set_repeat(1, 10) #tempo entre uma tecla e outra
        self.clock = self.ambiente.time.Clock()
        self.inicializar_cenario(img_mapa)
        self.criar_npc()
        self.criar_drop()
        self.ambiente.time_tiro = 0
        while jogar:
            self.clock.tick(self.clock_tick)
            self.ambiente.time_tiro += self.clock.get_time()
            self.cont += 1
            if not self.status_jogo():
                print("Você perdeu!")
                break
            jogar = self.tratar_eventos()
            self.atualizar_objetos()
            self.atualizar_tela()
            self.adicionar_drop_npc()
        self.ambiente.quit()
