# Model produto.py


from . import db

class Produto (db.Model):
    __tablename__ = 'produto'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    preco = db.Column(db.Float, nullable=False)
    categoria = db.Column(db.String(80), nullable=False)
