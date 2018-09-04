"""
Created on jun de 2017

@author: Adriano
@author: Andrei
@author: Joao
"""

from banco_de_dados.crud import Crud

class Conexao(Crud):
    """
    classe para a aocnexão entre o jogo e a crud
    """

    def __init__(self):
        """
            função inicia a função inicial da Crud
            :return: return da função chamada
        """
        super().__init__()

    def cadastrar_usuario(self, nome_usuario, senha):
        """
            função para cadastro de usuario
            :param nome_usuario:
            :param senha:
            :return: return da função chamada
        """
        return super().inserir_todos(nome_usuario, senha)

    def logar_usuario(self, usuario, senha):
        """
            função para login de usuario
            :param usuario:
            :param senha:
            :return: Se os dados não coincidirem, False. Senão, dados do usuario
        """
        dados = super().selecionar_usuario(usuario)
        print(dados)
        if dados[2] != senha or dados == None or dados == False:
            return False
        else:
            return dados

    def retornar_todos(self):
        """
        função para retornar todos os usuarios
        :return: dados dos usuarios
        """
        dados = super().selecionar_todos()
        return dados

    def atualizar_pontuacao(self, usuario, pontuacao):
        dados = super().selecionar_usuario(usuario)
        if dados[3] > pontuacao:
            return False
        else:
            sql = "UPDATE jogador SET record_usuario = '%d' WHERE nome_usuario = '%s'"%(pontuacao, usuario)
            super().executar_sql(sql)
            return True
