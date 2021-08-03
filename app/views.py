from app.dao.usuario_dao import UsuarioDao
from app.dao.carro_dao import CarroDao
from app import app
from flask import render_template, request, redirect, url_for, session
from app.models.carro import Carro



@app.route('/')
def lista_carros():
    
    if not session.get('username'):
        session['username'] = None

    carro_dao = CarroDao()
    carros = carro_dao.listar()
    
    if request.args.get('ID'):
        carro = carro_dao.detalhar(request.args.get('ID'))
        if type(carro) != str:
            carros = [carro]
        else:
            carros = []
    return render_template('index.html', carros=carros)


@app.route('/cadastro', methods=['GET','POST'])
def cadastro():
    if session['username'] is None:
        return redirect(url_for('lista_carros'))
        
    if request.method == 'POST':
        carro = Carro(0, request.form['Marca'], request.form['Modelo'],  request.form['Cor'],  request.form['Combustivel'],  request.form['Ano'] )
        CarroDao().cadastrar(carro)
        return redirect(url_for('lista_carros'))
    return render_template('form.html')

    
@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    if session['username'] is None:
        return redirect(url_for('lista_carros'))

    carro_dao = CarroDao()

    if request.method == 'POST':
        carro = Carro(id, request.form['Marca'], request.form['Modelo'],  request.form['Cor'],  request.form['Combustivel'],  request.form['Ano'] )
        carro_dao.atualizar(carro)
        return redirect(url_for('lista_carros'))

    carro = carro_dao.detalhar(id)
    if type(carro) == str:
        print(carro)
        return render_template('form.html', erro=carro)
    return render_template('form.html', id=carro.id, marca=carro.marca, modelo=carro.modelo, cor=carro.cor, combustivel=carro.combustivel, ano=carro.ano, delete=True)

@app.route('/deletar/<int:id>')
def deletar(id):
    if session['username'] is None:
        return redirect(url_for('lista_carros'))

    CarroDao().deletar(id)
    return redirect(url_for('lista_carros'))


@app.route('/login', methods=['GET', 'POST'])
def autenticar():
    if request.method == 'POST':
        autenticado = UsuarioDao().autenticar(request.form['username'], request.form['senha'])
        if autenticado:
            session['username'] = request.form['username']
            return redirect(url_for('lista_carros'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session['username'] = None
    return redirect(url_for('lista_carros'))



