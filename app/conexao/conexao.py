from psycopg2 import connect
from dotenv import dotenv_values


config = dotenv_values('.env')

class Conexao:
    def __init__(self):
        self.banco_de_dados = 'atividade-flask'
        self.usuario = 'postgres'
        self.senha = config.get('senha')
        self.host = 'localhost'
        self.porta = 5432


    def get_connection(self):
        return connect(f"dbname={self.banco_de_dados} user={self.usuario} password={self.senha} host={self.host} port={self.porta}")
