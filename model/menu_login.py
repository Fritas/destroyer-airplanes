"""
Created on jun de 2017

@author: Adriano
@author: Andrei
@author: Joao
"""
from tkinter import *
from dal.conexao import Conexao
from .gerenciarJogo import iniciar_jogo

class Login:
    """
    Esse metodo ira definir como sera a tela de login/acesso do usuario ao jogo
    """

    def __init__(self, root, nome_form, bg_cor):
        # * Método para definir algumas propriedades do tkinter ao contruir objeto
        self.master = root
        self.bg_cor = bg_cor
        self.fg_cor = '#cecece'
        self.cor = '#004a95'
        self.master.title(nome_form)  # Define o nome dado ao form de acordo com o valor de parametro
        self.master.geometry('260x210')  # Define a resolução da tela para 500x300
        self.master.config(bg = self.bg_cor)
        self.master.resizable()
        self.fonte = ('Verdana', '8')

        self.usuarios = [('teste','senha')] # Define um usuario de teste *nao precisa banco de dados*

        self.criar_area_login()

    def criar_area_login(self):
        # * Esse método irá criar os elementos necessários para fazer acesso
        self.lblusuario = Label(self.master, text = 'Usuario:', font = self.fonte, bg = self.bg_cor, fg = self.fg_cor)
        self.lblusuario.place(x = 25, y = 10)

        self.txtusuario = Entry(self.master, bg = self.bg_cor, fg = 'white', relief = GROOVE, highlightcolor = 'white',\
                                highlightthickness = 2, highlightbackground = self.cor, width = 20, font = 10, bd = 5)
        self.txtusuario.place(x = 25, y = 30)

        self.lblsenha = Label(self.master, text = 'Senha:', font = self.fonte, bg = self.bg_cor, fg = self.fg_cor)
        self.lblsenha.place(x = 25, y = 70)

        self.txtsenha = Entry(self.master, bg = self.bg_cor, fg = 'white', relief = GROOVE, highlightcolor = 'white',\
                              highlightthickness = 2, highlightbackground = self.cor, width = 20, font = 10, show = '*', bd = 5)
        self.txtsenha.place(x = 25, y = 90)

        self.aviso = Label(self.master, font = self.fonte, bg = self.bg_cor)
        self.aviso.place(x = 40, y = 130)

        self.entrar = Button(self.master, text = 'Login', bg = self.bg_cor, fg = self.fg_cor, relief = GROOVE,\
                             highlightcolor = self.cor, highlightthickness = 4, width = 18, font = 10, command = self.evento_entrar)
        self.entrar.place(x = 25, y = 150)

    #def criar_area_login(self):
    #    lista = [("Label", "Usuario: "), ("Label", "Senha: "), ("Button", "Login")]
    #    for tupla in lista:
    #        if tupla[0]

    def evento_entrar(self):
        """
            * Esse metodo serve para verificar o login sem utilizar o banco de dados,
            * eh um metodo de testes apenas, nao considerar 
        """

        senha = self.txtsenha.get()
        usuario = self.txtusuario.get()
        cnct = Conexao()
        jogador = cnct.logar_usuario(usuario, senha)
        if jogador:
            print("logado")
            #executar as funções de login sucesso
            #destruir o menu entrar
            self.master.destroy()
            #execua funcao que inicia o pygame e os metodos para o inicio do jogo
            iniciar_jogo(jogador)
        else:
            print("erro no login")
            #executar as funções de erro no login
