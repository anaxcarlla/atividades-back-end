from flask import Flask, request, jsonify

app = Flask(__name__)


user_data = {"id": 10, "name": "João", "email": "joao@email.com"}

@app.route('/usuario/10', methods=['GET'])
def get_user():
    return jsonify(user_data)

@app.route('/usuario/10', methods=['PUT'])
def update_user():
    data = request.json
    if "email" in data:
        user_data["email"] = data["email"]
        return jsonify({"message": "E-mail atualizado com sucesso"}), 200
    return jsonify({"error": "Dados inválidos"}), 400

if __name__ == '__main__':
    app.run(debug=True)
