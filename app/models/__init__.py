# models/__init__.py

from flask_sqlalchemy import SQLAlchemy

# Criação da instância do SQLAlchemy
db = SQLAlchemy()

# Importação dos modelos para que sejam reconhecidos pelo SQLAlchemy

from .produto import Produto
from .categoria import Categoria
