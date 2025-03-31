from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from app import db

# Tabela Projeto
class Projeto(db.Model):
    __tablename__ = "projeto"

    id           = Column(Integer, primary_key=True, index=True)
    nome         = Column(String, index=True, unique=True, nullable=False)
    descricao    = Column(String)
    status       = Column(String, default='Backlog')
    data_inicial = Column(Date)

    # Relacionamento com Atividade
    atividades = relationship("Atividade", back_populates="projeto", cascade="all, delete-orphan")

# Tabela Atividade
class Atividade(db.Model):
    __tablename__ = "atividade"

    id           = Column(Integer, primary_key=True, index=True)
    projeto_id   = Column(Integer, ForeignKey("projeto.id", ondelete="CASCADE"), nullable=False)
    titulo       = Column(String, nullable=False)
    descricao    = Column(String)
    status       = Column(String, default="Backlog")
    data_inicial = Column(Date)

    # Relacionamento com Projeto
    projeto = relationship("Projeto", back_populates="atividades")
