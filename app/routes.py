from flask import request, jsonify
from .openai_client import extrair_dados

def register_routes(app):

    @app.route("/", methods=["GET"])
    def index():
        return jsonify({"message": "API - ONLINE"})


    @app.route("/sendMessage", methods=["POST"])
    def extract():
        if not request.is_json:
            return jsonify({"error": "Content-Type deve ser application/json"}), 415

        data = request.get_json()
        texto = data.get("mensagem")

        if not texto:
            return jsonify({"error": "Campo 'mensagem' é obrigatório."}), 400

        try:
            resultado = extrair_dados(texto)
            return jsonify(resultado)
        except Exception as e:
            return jsonify({"error": str(e)}), 500
