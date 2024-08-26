# controllers/__init__.py

from flask import Blueprint
from .home import home_bp
from .produto import produto_bp

# Criação de um blueprint para o módulo controllers
controllers_bp = Blueprint('controllers', __name__)

# Registro dos blueprints dos controladores
controllers_bp.register_blueprint(home_bp)
controllers_bp.register_blueprint(produto_bp)

# Você pode adicionar mais controladores aqui, se necessário

