from flask import Flask, render_template, request, jsonify
from utils.ocr import extract_text_from_pdf
from utils.nlp import answer_question


def setup_routes(app):
    @app.route("/")
    def home():
    #     # return "Flask server is running!"
        return render_template('index.html')

    if __name__ == "__main__":
        # Get the PORT environment variable from Render or default to 5000
        port = int(os.environ.get("PORT", 5000))
        app.run(host="0.0.0.0", port=port)

    @app.route('/upload', methods=['POST'])
    def upload_document():
        file = request.files['file']
        text = extract_text_from_pdf(file)
        return jsonify({"text": text})

    @app.route('/ask', methods=['POST'])
    def ask_question():
        data = request.get_json()
        question = data.get('question')
        document_text = data.get('text')
        answer = answer_question(document_text, question)
        return jsonify({"answer": answer})

    @app.route('/upload_and_ask', methods=['POST'])
    def upload_and_ask():
        # Get the uploaded file and question from the request
        file = request.files.get('file')
        question = request.form.get('question')

        # Ensure both are provided
        if not file or not question:
            return jsonify({"error": "Please provide a PDF file and a question."}), 400

        try:
            # Extract text from the uploaded PDF
            document_text = extract_text_from_pdf(file)

            # Use NLP to answer the question
            answer = answer_question(document_text, question)

            return jsonify({
                "text": document_text,
                "answer": answer
            })
        except Exception as e:
            return jsonify({"error": str(e)}), 500
