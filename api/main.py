from flask import Flask, request, jsonify
from api.utils.ocr import extract_text_from_pdf
from api.utils.nlp import answer_question
from api.routes import setup_routes

app = Flask(__name__)

# Configuración inicial
app.config['UPLOAD_FOLDER'] = './uploads'

# Configurar las rutas
setup_routes(app)

if __name__ == "__main__":
    app.run(debug=True)
