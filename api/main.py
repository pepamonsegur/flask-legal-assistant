from flask import Flask, request, jsonify
from utils.ocr import extract_text_from_pdf
from utils.nlp import answer_question
from routes import setup_routes

app = Flask(__name__)

# Configuración inicial
app.config['UPLOAD_FOLDER'] = './uploads'

# Configurar las rutas
setup_routes(app)

# Required handler for Vercel's serverless environment
def handler(event, context):
    from flask_lambda import FlaskLambda
    return FlaskLambda(app)(event, context)
