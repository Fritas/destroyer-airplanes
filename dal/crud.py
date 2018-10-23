"""
Created on jun de 2017

@author: Adriano
@author: Andrei
@author: Joao
"""
import sqlite3

class Crud:
	"""
	    Classe que executa as iterações com o banco de dados SQLIITE
	"""

	def __init__(self):
		"""
			inicia chamando a função que cria uma conexão com um banco já definido
		"""
		self.connect_database()

	def connect_database(self):
		"""
        função realiza a conexão com o banco já definido e cria as variáveis para controle do mesmo
		:return: se a conexão for um sucesso, True. Se não, False
		"""
		try:
			self.conn = sqlite3.connect('database.db')
			self.cursor = self.conn.cursor()
			print("Conexão realizada com sucesso!")
			return True
		except sqlite3.Error:
			print("Erro ao conectar")
			return False

	def close_connection(self):
		"""
        função que realiza o fechamento da coneão com o banco, para que o mesmo não continue rodando em segundo plano
		:return: None
		"""
		if self.conn:
			self.conn.close()
			print("Conexão fechada com sucesso!")

	def selecionar_todos(self):
		"""
        Função seleciona todos os dados de todos os usuarios cadastrados no banco
		:return: Se sucesso, um array com todos os dados. Senão, False
		"""
		try:
			sql = "SELECT * FROM jogador"
			result = self.cursor.execute(sql)
			return result.fetchall()
		except sqlite3.Error:
			print(sqlite3.Error)
			print("Erro ao buscar")
			self.close_connection()
			return False

	def selecionar_usuario(self, nome_usuario):
		"""
        Função seleciona um usuário específico cadastrado no banco
        :param nome_usuario:
		:return: Se sucesso, um array com os dados do jogador solicitado. Senão, False
		"""
		try:
			sql = "SELECT * FROM jogador WHERE nome_usuario = '%s'"%(nome_usuario)
			result = self.cursor.execute(sql)
			return result.fetchone()
		except sqlite3.Error:
			self.close_connection()
			print("Erro ao buscar")
			return False

	def inserir_todos(self, usuario, senha):
		"""
        função para inserção de todos os dados na tabela jogador
        :param usuario: str
        :param senha: str
		:return: Se sucesso, True. Senão, False
		"""
		try:
			self.connect_database()
			sql = "INSERT INTO jogador (nome_usuario, senha_usuario) VALUES ('%s', '%s')" %(usuario, senha)
			self.cursor.execute(sql)
			self.conn.commit()
			return True

		except sqlite3.Error as error:
			print("Erro ao inserir: ", error)
			self.close_connection()
			return False

	def executar_sql(self, sql): #n pode ser um select
		"""
        função para execução de um código sql enviado, com exceção de selects
        :param sql:
        :retun: se sucesso, True. Senão, False
		"""
		try:
			self.connect_database()
			self.cursor.execute(sql)
			self.conn.commit()
			return True
		except sqlite3.Error:
			print("Erro")
			self.close_connection()
			return False

if __name__ == "__main__":
	crud = Crud()
	crud.inserir_todos('adriano123', '123')