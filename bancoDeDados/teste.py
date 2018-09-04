from conexao import Conexao
c = Conexao()
print(c.cadastrar_usuario('admin', 'admin'))
print(c.logar_usuario('admin', 'admin'))
print(c.retornar_todos())
print(c.atualizar_pontuacao('admin', 15))
