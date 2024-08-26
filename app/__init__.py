from flask import Flask

app = Flask(__name__)

from app.controllers import home, produto
from app.models import produto, categoria