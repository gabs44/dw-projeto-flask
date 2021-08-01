from psycopg2.extras import RealDictCursor
from app.models.carro import Carro
from app.conexao.conexao import Conexao

class CarroDao:

    def listar(self):
        conexao = Conexao().get_connection()
        cursor = conexao.cursor(cursor_factory=RealDictCursor)
        cursor.execute('select * from carros')
        resultado = cursor.fetchall()
        conexao.close()
        return converter_carros(resultado)

    def cadastrar(self, carro):
        conexao = Conexao().get_connection()
        cursor = conexao.cursor(cursor_factory=RealDictCursor)
        cursor.execute(f"insert into carros (marca, modelo,  cor, combustivel, ano) values ('{carro.marca}', '{carro.modelo}', '{carro.cor}', '{carro.combustivel}', '{carro.ano}')")
        conexao.commit()
        conexao.close()
        return True

    def atualizar(self, carro):
        conexao = Conexao().get_connection()
        cursor = conexao.cursor(cursor_factory=RealDictCursor)
        cursor.execute(f"update carros set marca = '{carro.marca}', modelo = '{carro.modelo}' , cor = '{carro.cor}', " \
                      f" combustivel = '{carro.combustivel}', ano = '{carro.ano}' where id = {carro.id} ")
        conexao.commit()
        conexao.close()
        return True


    def detalhar(self, id):
        conexao = Conexao().get_connection()
        cursor = conexao.cursor(cursor_factory=RealDictCursor)
        cursor.execute(f"select * from carros where id = {id}")
        resultado = cursor.fetchone()
        conexao.close()
        if resultado is None:
            return 'Esse ID não existe'
        return converter_carro(resultado)


    def deletar(self, id):
        conexao = Conexao().get_connection()
        cursor = conexao.cursor(cursor_factory=RealDictCursor)
        cursor.execute(f"delete from carros where id = {id} ")
        conexao.commit()
        conexao.close()
        return True



def converter_carro(objeto):
    return Carro(objeto.get('id'), objeto.get('marca'), objeto.get('modelo'), objeto.get('cor'),
                objeto.get('combustivel'), objeto.get('ano'))

def converter_carros(lista):
    resultados=[]
    for objeto in lista:
        resultado = converter_carro(objeto)
        resultados.append(resultado)
    return resultados

