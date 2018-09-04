from tkinter import *
from PIL import Image, ImageTk
from menu_login import Login
from menu_registrar import Registro

class Menu:
    '''
    Essa classe ira definir como sera o menu do jogo
    '''

    def __init__(self, root, nome_form, bg_cor):

        self.master = root
        self.bg_cor = bg_cor
        self.master.title(nome_form) #Define o nome dado ao form de acordo com o valor de parametro
        self.master.geometry('500x500') #Define a resolução da tela para 500x500

        self.canvas = Canvas(self.master, width = 500, height = 500, highlightthickness = 0)
        self.canvas.pack()

        self.fonte = ('Verdana', '8')

        self.criar_mainmenu()

    def criar_mainmenu(self):
        '''
          * Esse metodo ira criar o menu principal
          * Adiciona uma background super bacana ao menu:
        '''
        self.background_n = Image.open("../img/menu/background.gif")
        self.background_n = self.background_n.resize((int(500), int(500)), Image.ANTIALIAS)
        self.bg_render = ImageTk.PhotoImage(self.background_n)
        self.bg_img = Label(self.canvas, image = self.bg_render, borderwidth = 0)
        self.bg_img.image = self.bg_render
        self.bg_img.place(x = int(0), y = int(0))
        # * Adiciona o logo/titulo do menu:
        self.titulo_n = Image.open("../img/menu/titulo.gif")
        self.titulo_n = self.titulo_n.resize((int(375), int(50)), Image.ANTIALIAS)
        self.titulo_render = ImageTk.PhotoImage(self.titulo_n)
        self.titulo_img = Label(self.canvas, image = self.titulo_render, borderwidth = 0)
        self.titulo_img.image = self.titulo_render
        self.titulo_img.place(x = 75, y = 50)
        self.titulo_img.lift()
        # * Adiciona um botao para iniciar o jogo:
        self.iniciar_n = Image.open("../img/menu/botoes/iniciar.gif")
        self.iniciar_n = self.iniciar_n.resize((int(175), int(40)), Image.ANTIALIAS)
        self.iniciar_render = ImageTk.PhotoImage(self.iniciar_n)
        self.iniciar_img = Label(self.canvas, image = self.iniciar_render, borderwidth = 0)
        self.iniciar_img.image = self.iniciar_render
        self.iniciar_img.place(x = 175, y = 150)
        self.iniciar_img.bind("<Button-1>", lambda s : self.mostrar_iniciar_jogo())
        self.iniciar_img.lift()
        # * Adiciona um botao para ver o ranking do jogo:
        self.ranking_n = Image.open("../img/menu/botoes/ranking.gif")
        self.ranking_n = self.ranking_n.resize((int(175), int(40)), Image.ANTIALIAS)
        self.ranking_render = ImageTk.PhotoImage(self.ranking_n)
        self.ranking_img = Label(self.canvas, image = self.ranking_render, borderwidth = 0)
        self.ranking_img.image = self.ranking_render
        self.ranking_img.place(x = 175, y = 195)
        self.ranking_img.bind("<Button-1>", lambda s : self.mostrar_ranking())
        self.ranking_img.lift()
        # * Adiciona os creditos do jogo:
        self.creditos_n = Image.open("../img/menu/botoes/creditos.gif")
        self.creditos_n = self.creditos_n.resize((int(175), int(40)), Image.ANTIALIAS)
        self.creditos_render = ImageTk.PhotoImage(self.creditos_n)
        self.creditos_img = Label(self.canvas, image = self.creditos_render, borderwidth = 0)
        self.creditos_img.image = self.creditos_render
        self.creditos_img.place(x = 175, y = 240)
        self.creditos_img.bind("<Button-1>", lambda s : self.mostrar_creditos())
        self.creditos_img.lift()
        # * Adiciona a caixa de créditos do jogo (submenu Creditos):
        self.img_creditos_n = Image.open("../img/menu/creditos.gif")
        self.img_creditos_n = self.img_creditos_n.resize((int(175), int(175)), Image.ANTIALIAS)
        self.img_creditos_render = ImageTk.PhotoImage(self.img_creditos_n)
        self.img_creditos_img = Label(self.canvas, image = self.img_creditos_render, borderwidth = 0)
        self.img_creditos_img.image = self.img_creditos_render
        self.img_creditos_img.place(x = 175, y = 150)
        self.img_creditos_img.lower()

        # * Adiciona um botao de sair:
        self.sair_n = Image.open("../img/menu/botoes/sair.gif")
        self.sair_n = self.sair_n.resize((int(175), int(40)), Image.ANTIALIAS)
        self.sair_render = ImageTk.PhotoImage(self.sair_n)
        self.sair_img = Label(self.canvas, image = self.sair_render, borderwidth = 0)
        self.sair_img.image = self.sair_render
        self.sair_img.place(x = 175, y = 330)
        self.sair_img.bind("<Button-1>", lambda s : self.evento_sair())
        self.sair_img.lift()
        # * Adiciona um botao de voltar menu principal:
        self.voltarmain_n = Image.open("../img/menu/botoes/voltar.gif")
        self.voltarmain_n = self.voltarmain_n.resize((int(175), int(40)), Image.ANTIALIAS)
        self.voltarmain_render = ImageTk.PhotoImage(self.voltarmain_n)
        self.voltarmain_img = Label(self.canvas, image = self.voltarmain_render, borderwidth = 0)
        self.voltarmain_img.image = self.voltarmain_render
        self.voltarmain_img.place(x = 175, y = 330)
        self.voltarmain_img.bind("<Button-1>", lambda s : self.evento_voltar_mainmenu())
        self.voltarmain_img.lower()
        # * Adiciona um botao de voltar submenu iniciar:
        self.voltarini_n = Image.open("../img/menu/botoes/voltar.gif")
        self.voltarini_n = self.voltarini_n.resize((int(175), int(40)), Image.ANTIALIAS)
        self.voltarini_render = ImageTk.PhotoImage(self.voltarini_n)
        self.voltarini_img = Label(self.canvas, image=self.voltarini_render, borderwidth=0)
        self.voltarini_img.image = self.voltarini_render
        self.voltarini_img.place(x=175, y=330)
        self.voltarini_img.bind("<Button-1>", lambda s: self.evento_voltar_submenu_iniciar())
        self.voltarini_img.lower()
        # * Adiciona um botao de voltar submenu ranking:
        self.voltarank_n = Image.open("../img/menu/botoes/voltar.gif")
        self.voltarank_n = self.voltarank_n.resize((int(175), int(40)), Image.ANTIALIAS)
        self.voltarank_render = ImageTk.PhotoImage(self.voltarank_n)
        self.voltarank_img = Label(self.canvas, image=self.voltarank_render, borderwidth=0)
        self.voltarank_img.image = self.voltarank_render
        self.voltarank_img.place(x=175, y=330)
        self.voltarank_img.bind("<Button-1>", lambda s: self.evento_voltar_submenu_ranking())
        self.voltarank_img.lower()
        # * Adiciona um botão do top +10 (submenu Ranking):
        self.top10mais_n = Image.open("../img/menu/botoes/top10mais.gif")
        self.top10mais_n = self.top10mais_n.resize((int(175), int(40)), Image.ANTIALIAS)
        self.top10mais_render = ImageTk.PhotoImage(self.top10mais_n)
        self.top10mais_img = Label(self.canvas, image=self.top10mais_render, borderwidth=0)
        self.top10mais_img.image = self.top10mais_render
        self.top10mais_img.place(x=175, y=150)
        self.top10mais_img.bind("<Button-1>", lambda s : self.mostrar_top10mais())
        self.top10mais_img.lower()
        # * Adiciona um botão do top -10 (submenu Ranking):
        self.top10menos_n = Image.open("../img/menu/botoes/top10menos.gif")
        self.top10menos_n = self.top10menos_n.resize((int(175), int(40)), Image.ANTIALIAS)
        self.top10menos_render = ImageTk.PhotoImage(self.top10menos_n)
        self.top10menos_img = Label(self.canvas, image=self.top10menos_render, borderwidth=0)
        self.top10menos_img.image = self.top10menos_render
        self.top10menos_img.place(x=175, y=195)
        self.top10menos_img.bind("<Button-1>", lambda s : self.mostrar_top10menos())
        self.top10menos_img.lower()
        # * Adiciona um botao de entrar/login (submenu Iniciar Jogo):
        self.entrar_n = Image.open("../img/menu/botoes/entrar.gif")
        self.entrar_n = self.entrar_n.resize((int(175), int(40)), Image.ANTIALIAS)
        self.entrar_render = ImageTk.PhotoImage(self.entrar_n)
        self.entrar_img = Label(self.canvas, image=self.entrar_render, borderwidth=0)
        self.entrar_img.image = self.entrar_render
        self.entrar_img.place(x=175, y=150)
        self.entrar_img.bind("<Button-1>", lambda s : self.mostrar_entrar())
        self.entrar_img.lower()
        # * Adiciona um botao de registro (submenu Iniciar Jogo):
        self.registro_n = Image.open("../img/menu/botoes/registrar.gif")
        self.registro_n = self.registro_n.resize((int(175), int(40)), Image.ANTIALIAS)
        self.registro_render = ImageTk.PhotoImage(self.registro_n)
        self.registro_img = Label(self.canvas, image=self.registro_render, borderwidth=0)
        self.registro_img.image = self.registro_render
        self.registro_img.place(x=175, y=195)
        self.registro_img.bind("<Button-1>", lambda s : self.mostrar_registro())
        self.registro_img.lower()

    def mostrar_iniciar_jogo(self):
        '''
          * Esse método irá mostrar o submenu iniciar do jogo
          * Esconder menu principal: '''
        self.evento_esconder_mainmenu()
        self.evento_esconder_submenu_ranking()
        self.voltarini_img.lower()
        self.voltarank_img.lower()
        # * Mostrar img botão entrar, registrar e voltar, respectivamente:
        self.entrar_img.lift()
        self.registro_img.lift()
        self.voltarmain_img.lift()
        print('Debug: mostrando submenu iniciar...')

    def mostrar_entrar(self):
        '''
          * Esse método irá mostrar a área de acesso do usuário ao jogo
          * Esconder menu principal, botão entrar e registrar, respectivamente: '''
        self.evento_esconder_mainmenu()
        self.evento_esconder_submenu_iniciar()
        self.evento_esconder_submenu_ranking()
        # * Mostrar botão voltar:
        self.voltarini_img.lift()
        # * Área de login:
        self.criar_campo_login()
        self.evento_voltar_submenu_iniciar()
        print('Debug: mostrando área de acesso...')

    def mostrar_registro(self):
        '''
          * Esse método irá mostrar a área de registro do usuário ao jogo
          * Esconder menu principal, botão registrar e entrar, respectivamente: '''
        self.evento_esconder_mainmenu()
        self.evento_esconder_submenu_iniciar()
        self.evento_esconder_submenu_ranking()
        # * Mostrar botão voltar:
        self.voltarini_img.lift()
        # * Área de registro
        self.criar_campo_registro()
        print('Debug: mostrando área de registro...')

    def mostrar_ranking(self):
        '''
          * Esse método irá mostrar o submenu de ranking do jogo
          * Esconder menu principal: '''
        self.evento_esconder_mainmenu()
        # * Mostrar img botão top +10, -10, voltar, respectivamente:
        self.top10mais_img.lift()
        self.top10menos_img.lift()
        self.voltarmain_img.lift()
        print('Debug: mostrando submenu ranking...')

    def mostrar_top10mais(self):
        '''
          * Esse método irá mostrar o ranking dos melhores jogadores
          * Esconder menu principal, botão +10, botão -10, respectivamente: '''
        self.evento_esconder_mainmenu()
        self.evento_esconder_submenu_ranking()
        self.evento_esconder_submenu_iniciar()
        # * Mostrar img botão voltar:
        self.voltarank_img.lift()
        # * Área do ranking dos melhores jogadores:
        print('Debug: mostrando os melhores jogadores...')

    def mostrar_top10menos(self):
        '''
          * Esse método irá mostrar o ranking dos piores jogadores
          * Esconder menu principal, botão +10, botão 10, respectivamente: '''
        self.evento_esconder_mainmenu()
        self.evento_esconder_submenu_ranking()
        self.evento_esconder_submenu_iniciar()
        # * Mostrar img botão voltar:
        self.voltarank_img.lift()
        # * Área do ranking dos piores jogadores:
        print('Debug: mostrando os piores jogadores...')

    def mostrar_creditos(self):
        '''
          * Esse método irá mostrar os créditos do jogo
          * Esconder menu principal: '''
        self.evento_esconder_mainmenu()
        # * Mostrar img caixa de créditos do jogo e botão voltar, respectivamente:
        self.img_creditos_img.lift()
        self.voltarmain_img.lift()
        print('Debug: mostrando créditos do jogo...')

    def criar_campo_login(self):
        root = Tk()
        root.wm_attributes("-topmost", True)
        root.wm_attributes("-alpha", 1)
        Login(root, 'Entrar','#282828')

    def criar_campo_registro(self):
        print("Debug: mostrando tela registro")
        root = Tk()
        root.wm_attributes("-topmost", True)
        root.wm_attributes("-alpha", 1)
        Registro(root, 'Registrar','#282828')
        self.evento_voltar_submenu_iniciar()

    def criar_campo_melhores(self):
        pass

    def criar_campo_piores(self):
        pass

    def evento_sair(self):
        # * Esse método irá fechar a interface do jogo
        self.master.destroy()

    def evento_esconder_mainmenu(self):
        # * Esse método esconde as imagens do menu principal, deixando apenas titulo
        self.iniciar_img.lower()
        self.ranking_img.lower()
        self.creditos_img.lower()
        self.sair_img.lower()

    def evento_esconder_submenu_iniciar(self):
        # * Esse método esconde as imagens do submenu iniciar jogo, deixando apenas titulo e botão voltar
        self.entrar_img.lower()
        self.registro_img.lower()

    def evento_esconder_submenu_ranking(self):
        # * Esse método esconde as imagens do submenu ranking, deixando apenas titulo e botão voltar
        self.top10mais_img.lower()
        self.top10menos_img.lower()

    def evento_voltar_mainmenu(self):
        '''
          * Método para voltar ao menu principal
          * Esconder imgs creditos: '''
        self.img_creditos_img.lower()
        # * Esconder imgs submenu iniciar:
        self.evento_esconder_submenu_iniciar()
        # * Esconder imgs submenu ranking:
        self.evento_esconder_submenu_ranking()
        # * Esconder imgs evento voltar:
        self.voltarmain_img.lower()
        self.voltarini_img.lower()
        self.voltarank_img.lower()
        # * Mostrar imgs main menu:
        self.iniciar_img.lift()
        self.ranking_img.lift()
        self.creditos_img.lift()
        self.sair_img.lift()
        print('Debug: voltando para o menu principal...')

    def evento_voltar_submenu_iniciar(self):
        '''
          * Método para voltar ao submenu iniciar
          * Esconder imgs botão voltar: '''
        self.voltarini_img.lower()
        # * Mostrar imgs botão submenu iniciar:
        self.entrar_img.lift()
        self.registro_img.lift()
        self.voltarmain_img.lift()
        print('Debug: voltando para o submenu iniciar...')

    def evento_voltar_submenu_ranking(self):
        '''
          * Método para voltar ao submenu ranking
          * Esconder imgs botão voltar: '''
        self.voltarank_img.lower()
        # * Mostrar imgs submenu ranking:
        self.top10mais_img.lift()
        self.top10menos_img.lift()
        self.voltarmain_img.lift()
        print('Debug: voltando para o submenu ranking...')
