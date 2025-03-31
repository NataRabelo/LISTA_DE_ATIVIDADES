import datetime
from flask import Blueprint, flash, redirect, render_template, request, url_for
from app.models import Atividade, Projeto
from app import db

projeto = Blueprint('projeto', __name__)

@projeto.route('/criar_projeto', methods=['GET', 'POST'])
def criar_projeto():
    if request.method == 'POST':
        nome = request.form.get('projectName')
        descricao = request.form.get('projectDescription')
        status = "Backlog"
        
        # Data e hora atuais
        data_inicial = datetime.datetime.now()

        projeto = Projeto(
            nome=nome,
            descricao=descricao,
            status=status,
            data_inicial=data_inicial
        )

        db.session.add(projeto)
        db.session.commit()

        projetos = Projeto.query.all()

        flash("Projeto Criado com sucesso", "success")
        return render_template('index.html', projetos=projetos)

    return redirect(url_for('main.index'))

@projeto.route('/detalhe_projeto/<int:id>', methods=['GET', 'POST'])
def detalhe_projeto(id):
    projeto = Projeto.query.get_or_404(id)
    atividades = Atividade.query.filter_by(projeto_id=id).all()
    return render_template('projeto.html', projeto=projeto, atividades=atividades)


@projeto.route('/editar_projeto/<int:id>', methods=['GET', 'POST'])
def editar_projeto(id):
    if request.method == 'POST':
        
        # Buscar o projeto pelo ID
        projeto = Projeto.query.get_or_404(id)
        
        # Atualizar os dados do projeto
        projeto.nome = request.form.get('projectName')
        projeto.descricao = request.form.get('projectDescription')
        
        # Salvar as alterações no banco de dados
        db.session.commit()

        # Redirecionar para a página de detalhes do projeto, passando o ID
        return redirect(url_for('projeto.detalhe_projeto', id=id))
    
    # Para o método GET, você pode retornar o formulário com os dados existentes
    projeto = Projeto.query.get_or_404(id)
    return render_template('editar_projeto.html', projeto=projeto)

@projeto.route('/listar_projeto', methods=['GET', 'POST'])
def listar_projeto():
    projetos = Projeto.query.all()
    return render_template(url_for('main.index'))

@projeto.route('/excluir_projeto/<int:id>', methods=['GET', 'POST'])
def excluir_projeto(id):
    projeto = Projeto.query.get_or_404(id)
    db.session.delete(projeto)
    db.session.commit()
    flash("Projeto deletado com sucesso")
    return redirect(url_for('main.index'))

@projeto.route('/concluir_projeto/<int:id>', methods=['GET', 'POST'])
def concluir_projeto(id):
    
    projeto = Projeto.query.get_or_404(id)
    projeto.status = 'Concluido'
    db.session.commit()
    return redirect(url_for('main.index'))

@projeto.route('/reabrir_projeto/<int:id>', methods=['GET', 'POST'])
def reabrir_projeto(id):
    
    projeto = Projeto.query.get_or_404(id)
    projeto.status = 'Backlog'
    db.session.commit()
    return redirect(url_for('main.index'))

@projeto.route('/executar_projeto/<int:id>', methods=['GET', 'POST'])
def executar_projeto(id):
    
    projeto = Projeto.query.get_or_404(id)
    projeto.status = 'Em andamento'
    db.session.commit()
    return redirect(url_for('main.index'))