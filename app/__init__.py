from flask import Flask
from dotenv import dotenv_values
config = dotenv_values('.env')
app = Flask(__name__)
app.secret_key = config['secret_key']

from app import views