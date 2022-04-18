from flask import Flask, request, render_template, make_response, jsonify
import json

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/save", methods=["POST"])
def save():
    
    try:
        data = request.values.to_dict()
        return make_response(jsonify({"message": "Usuario cadastrado com sucesso", "users": data}), 200)
        
    except Exception as ex:
        print(ex)
        return make_response(jsonify({"message": "Erro ao cadastrar usuário"}), 400)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3001, debug=True)
