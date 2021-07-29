from app import app
from flask import render_template
from app.models.carro import Carro


carros=[
    Carro(8679889, 'gol', 'bolinha', 'vermelho', 'gasolina', 2009),
    Carro(5736879, 'fiat', 'toro', 'preto', 'gasolina', 2021),
    Carro(2143546, 'honda', 'civic', 'branco', 'diesel', 2017),
    ]



@app.route('/')
def lista_carros():
    return render_template('index.html', carros=carros)

