from flask import Flask, Blueprint, render_template, redirect,request
from . import db
from .Model import Fruta
from datetime import datetime, date

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    frutas = Fruta.query.all()
    
    return render_template('index.html', frutas=frutas)

@main_bp.route('/cadastrar_fruta', methods=['GET', 'POST'])
def cadastrar_fruta():
    if request.method == 'GET':
        return render_template('cadastrar_fruta.html')
    else:
        nome = request.form['nome']
        preco = float(request.form['preco'].replace(',','.'))
        dataColheita = datetime.strptime(request.form['dataColheita'], '%Y-%m-%d').date()   
        dataVencimento = datetime.strptime(request.form['dataVencimento'], '%Y-%m-%d').date()
        descricao = request.form['descricao']
        
        fruta = Fruta(nome=nome, preco=preco, dataColheita=dataColheita, dataVencimento=dataVencimento, descricao=descricao)
        
        db.session.add(fruta)
        db.session.commit()
        
        return redirect('/')

@main_bp.route('/deletar_fruta/<int:id>')
def deletar_fruta(id):
    fruta = Fruta.query.filter_by(id=id).first()
    
    db.session.delete(fruta)
    db.session.commit()
    
    return redirect('/')

@main_bp.route('/editar/<int:id>')
def editar_fruta(id):
    fruta = Fruta.query.filter_by(id=id).first()
    return render_template('editar.html', fruta=fruta)

@main_bp.route('/atualizar', methods=['POST'])
def atualizar_fruta():
    id = int(request.args['id'])
    nome = request.form['nome']
    preco = float(request.form['preco'].replace(',','.'))
    dataColheita = datetime.strptime(request.form['dataColheita'], '%Y-%m-%d').date()   
    dataVencimento = datetime.strptime(request.form['dataVencimento'], '%Y-%m-%d').date()
    descricao = request.form['descricao']
    
    fruta = Fruta.query.filter_by(id=id).first()
    fruta.nome = nome
    fruta.preco = preco
    fruta.dataColheita = dataColheita
    fruta.dataVencimento = dataVencimento
    fruta.descricao = descricao
    
    db.session.commit()
    
    return redirect('/')