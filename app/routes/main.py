from flask import Blueprint, render_template

from app.models import Projeto

main = Blueprint('main', __name__)

@main.route('/')
def index():
    projetos = Projeto.query.all()
    return render_template('index.html', projetos=projetos)