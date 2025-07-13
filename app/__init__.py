import os
from flask import Flask
from flask_wtf.csrf import CSRFProtect


csrf = CSRFProtect()

app = Flask(__name__)
csrf.init_app(app)
app.config['SECRET_KEY'] = os.urandom(32)   


from app import routes


