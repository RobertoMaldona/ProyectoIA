from flask import Flask

UPLOAD_FOLDER = '../app1-uploads/'

app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
API_URL = 'http://gate.dcc.uchile.cl:8635/ejercicio-3a-ia/'