# controllers/produto.py

from flask import Blueprint, render_template

produto_bp = Blueprint('produto', __name__)

@produto_bp.route('/produto')
def produto():
    return render_template('produto.html')
