import os
import json
from app import app, API_URL
import requests
from flask import request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from utils import allowed_file
import secrets

@app.route('/', methods=['GET'])
def get_index():
    results = list()
    """
    apicall = requests.get(API_URL)
    if apicall.status_code == 200:
        #procesar resutlados
        pass
    """
    results.append("1min")
    results.append("2min")
    return render_template('index.html', results=results)
    
        

"""
@app.route('/', methods=['POST'])
def index_image():
    if 'file' not in request.files:
        error = 'No se envió ningún archivo'
        return render_template('index.html', error=error)
    file = request.files['file']
    if file.filename == '':
        error = 'No se seleccionó ningún archivo'
        return render_template('index.html', error=error)
    if file and allowed_file(file.filename):
        # Crear un directorio en UPLOAD_FOLDER cuando no exista
        if not os.path.exists(app.config['UPLOAD_FOLDER']):
            os.makedirs(app.config['UPLOAD_FOLDER'])

        # hash para evitar sobreescribir
        filename = secrets.token_hex(nbytes=8) + '_' + secure_filename(file.filename)
        # Get the directory where Flask looks for static files
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        files = {'file': open(filepath, 'rb')}
        print(files)
        apicall = requests.post(API_URL, files=files)
        if apicall.status_code == 200:
            error = None
            apicall = json.loads(apicall.content.decode('utf-8'))
            result = {'predicted_label': apicall['class_name'], 'class_id': apicall['class_id']}
        else:
            error = 'Error al procesar la imagen'
            result = {'predicted_label': None, 'class_id': None}
        return render_template('index.html', filename=filename, result=result, error=error)
    else:
        error = 'Archivo no permitido. Solo se permite JPG, JPEG o PNG.'
        return render_template('index.html', error=error)
"""

@app.route('/display/<filename>')
def display_image(filename):
    return redirect(url_for('static', filename='uploads/' + filename), code=301)


if __name__ == "__main__":
    app.run(port=5000)
