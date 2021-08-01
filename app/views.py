from app.dao.carro_dao import CarroDao
from app import app
from flask import render_template
from app.models.carro import Carro


@app.route('/')
def lista_carros():
    carro_dao = CarroDao()
    carros = carro_dao.listar()
    return render_template('index.html', carros=carros)


@app.route('/cadastro')
def cadastro():
    return render_template('form.html')

