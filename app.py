from flask import Flask,render_template
from dotenv import load_dotenv
import os
app = Flask(__name__)

app.secret_key = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/produtos')
def index():
    return render_template('produtos.html')

if __name__ == "__main__":
    app.run(debug=True)
