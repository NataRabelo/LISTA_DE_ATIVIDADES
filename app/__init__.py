from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    from app import models  # Importa o arquivo models.py corretamente
    from app.routes.main import main
    from app.routes.projeto import projeto 
    from app.routes.atividade import atividade

    app.register_blueprint(main)
    app.register_blueprint(projeto)
    app.register_blueprint(atividade)

    return app  
