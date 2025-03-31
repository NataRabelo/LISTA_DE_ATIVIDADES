import datetime
from flask import Blueprint, flash, redirect, render_template, request, url_for
from app.models import Atividade
from app import db

atividade = Blueprint('atividade', __name__)

@atividade.route('/criar_atividade', methods=['POST'])
def criar_atividade():
    projeto_id = request.form.get('projeto_id')  # Captura o ID do projeto
    titulo = request.form.get('titulo')
    descricao = request.form.get('descricao')
    data_inicial = datetime.datetime.now()

    if not projeto_id:
        flash('Erro: Projeto não encontrado.', 'danger')
        return redirect(url_for('home'))  # Redireciona para a home ou outra página de erro

    atividade = Atividade(
        projeto_id=projeto_id,  # Agora está definido corretamente
        titulo=titulo,
        descricao=descricao,
        data_inicial=data_inicial
    )

    db.session.add(atividade)
    db.session.commit()

    flash('Atividade criada com sucesso', 'success')

    # Redirecionar para a tela de detalhes do projeto atualizado
    return redirect(url_for('projeto.detalhe_projeto', id=projeto_id))

@atividade.route('/editar_atividade/<int:id>', methods=['GET', 'POST'])
def editar_atividade(id):

    atividade = Atividade.query.get_or_404(id)

    projeto_id = request.form.get('projeto_id')

    if not projeto_id:
        flash('Erro: Projeto não encontrado.', 'danger')
        return redirect(url_for('home'))

    atividade.titulo = request.form.get('titulo')
    atividade.descricao = request.form.get('descricao')

    db.session.commit()

    flash('Atividade editada com sucesso', 'success')
    return redirect(url_for('projeto.detalhe_projeto', id=projeto_id))

@atividade.route('/deletar_atividade/<int:id>', methods=['GET', 'POST'])
def deletar_atividade(id):
    atividade = Atividade.query.get_or_404(id)
    projeto_id = atividade.projeto_id
    db.session.delete(atividade)
    db.session.commit()
    return redirect(url_for('projeto.detalhe_projeto', id=projeto_id))

@atividade.route('/aprovar_atividade/<int:id>', methods=['GET', 'POST'])
def aprovar_atividade(id):
    
    atividade = Atividade.query.get_or_404(id)
    projeto_id = atividade.projeto_id
    atividade.status = 'Concluida'
    db.session.commit()
    return redirect(url_for('projeto.detalhe_projeto', id=projeto_id))

@atividade.route('/executar_atividade/<int:id>', methods=['GET', 'POST'])
def executar_atividade(id):
    
    atividade = Atividade.query.get_or_404(id)
    projeto_id = atividade.projeto_id
    atividade.status = 'Em andamento'
    db.session.commit()
    return redirect(url_for('projeto.detalhe_projeto', id=projeto_id))

@atividade.route('/reabrir_atividade/<int:id>', methods=['GET', 'POST'])
def reabrir_atividade(id):
    
    atividade = Atividade.query.get_or_404(id)
    projeto_id = atividade.projeto_id
    atividade.status = 'Backlog'
    db.session.commit()
    return redirect(url_for('projeto.detalhe_projeto', id=projeto_id))