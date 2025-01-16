from flask import Flask, request, jsonify
from utils.ocr import extract_text_from_pdf
from utils.nlp import answer_question
from routes import setup_routes

app = Flask(__name__)

# Configuración inicial
app.config['UPLOAD_FOLDER'] = './uploads'
app.secret_key = ''

# Configurar las rutas
setup_routes(app)

if __name__ == '__main__':
    app.run(debug=True)


from flask import Flask
