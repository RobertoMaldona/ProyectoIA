from app import app
from utils import contar_personas, elegir_archivo_al_azar
from flask import Flask, jsonify, request


import time

@app.route('/predict', methods=['GET'])
def predict():
    startTime = time.time()
    if request.method == 'GET':

        image_path = elegir_archivo_al_azar('media/micro1') 

        n_personas, tiempo = contar_personas(image_path)
        response = jsonify({'numero_personas': n_personas, 'tiempo': tiempo})
        print('Resultado ' + response +'\n') # esto no imprimira el resultado en si, si se quiere esto se deberia hacer json.dumps(response)
       
        endTime = time.time()
        elaspedTime = endTime - startTime
        print('Tiempo: ' + elaspedTime + ' segundos\n')
        return response


if __name__ == "__main__":
    app.run(port=5003)
