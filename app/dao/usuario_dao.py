from psycopg2.extras import RealDictCursor
from app.conexao.conexao import Conexao


class UsuarioDao:
    def autenticar(self, username, senha):
        conexao = Conexao().get_connection()
        cursor = conexao.cursor(cursor_factory=RealDictCursor)
        cursor.execute(f"select * from usuarios where username = '{username}' and senha = '{senha}' ")
        usuario = cursor.fetchone()
        if usuario is None:
            return False
        return True
