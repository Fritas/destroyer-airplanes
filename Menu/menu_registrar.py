from tkinter import *
from bancoDeDados.conexao import Conexao

class Registro:
    '''
    Esse método irá definir como será a tela de registro do usuario ao jogo
    '''


    def __init__(self, root, nome_form, bg_cor):
        # * Método para definir algumas propriedades do tkinter ao contruir objeto
        self.master = root
        self.bg_cor = bg_cor
        self.fg_cor = '#cecece'
        self.cor = '#004a95'
        self.master.title(nome_form)  # Define o nome dado ao form de acordo com o valor de parametro
        self.master.geometry('300x300')  # Define a resolução da tela para 500x300
        self.master.config(bg = self.bg_cor)
        self.master.resizable()
        self.fonte = ('Verdana', '8')
        self.criar_area_registro()

    def criar_area_registro(self):
        # * Esse método irá criar os elementos necessários para fazer o registro
        #fg eh cor da fonte, bg cor do fundo

        self.lblusuario = Label(self.master, text = 'Usuário:', font = self.fonte, bg = self.bg_cor, fg = self.fg_cor)
        self.lblusuario.place(x = 25, y = 10)

        self.txtusuario = Entry(self.master, bg = self.bg_cor, fg = 'white', relief = GROOVE, highlightcolor = 'white',\
                                highlightthickness = 2, highlightbackground = self.cor, width = 20, font = 10, bd = 5)
        self.txtusuario.place(x = 25, y = 30)

        self.lblsenha = Label(self.master, text = 'Senha:', font = self.fonte, bg = self.bg_cor, fg = self.fg_cor)
        self.lblsenha.place(x = 25, y = 70)

        self.txtsenha = Entry(self.master, bg = self.bg_cor, fg = 'white', relief = GROOVE, highlightcolor = 'white',\
                              highlightthickness = 2, highlightbackground = self.cor, width = 20, font = 10, show = '*', bd = 5)
        self.txtsenha.place(x = 25, y = 90)

        self.lbl_confirm_senha = Label(self.master, text = 'Confirmar Senha:', font = self.fonte, bg = self.bg_cor, fg = self.fg_cor)
        self.lbl_confirm_senha.place(x = 25, y = 130)

        self.txt_confirm_senha = Entry(self.master, bg = self.bg_cor, fg = 'white', relief = GROOVE, highlightcolor = 'white',\
                              highlightthickness = 2, highlightbackground = self.cor, width = 20, font = 10, show = '*', bd = 5)
        self.txt_confirm_senha.place(x = 25, y = 150)


        self.aviso = Label(self.master, text='Senha inválida!', font=self.fonte, fg=self.bg_cor, bg=self.bg_cor)
        self.aviso.place(x = 40, y = 190)

        self.registrar = Button(self.master, text = 'Registrar', bg = self.bg_cor, fg = self.fg_cor, relief = GROOVE,\
                                highlightcolor = self.cor, highlightthickness = 4, width=18, font=10, command = self.evento_registrar)
        self.registrar.place(x = 25, y = 210)

    def evento_registrar(self):
        confirmar_senha = self.txt_confirm_senha.get()
        senha = self.txtsenha.get()
        usuario = self.txtusuario.get()
        cnxo = Conexao()
        #validar senha
        if self.validar_senha(senha, confirmar_senha):
            self.aviso.config(fg=self.bg_cor)
            # codigo para cadastrado com sucesso
            if cnxo.cadastrar_usuario(usuario, senha):
                # destruir o menu registrar
                print("cadastrado")
                self.master.destroy()
            # codigo para erro no cadastro
            else:
                print("nao-cadastrado")
        else:
            self.aviso.config(fg='red')

    def validar_senha(self, senha, confirmar_senha):
        if confirmar_senha == senha:
            return True
        return False