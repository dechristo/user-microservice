from flask import Flask, jsonify, request, abort
from src.controllers.user_controller import UserController


app = Flask(__name__)
user_controller = UserController()

@app.route("/api/status-check")
def status_check():
    return jsonify({'msg':'user microservice running...'})

@app.route("/api/user", methods=['POST'])
def add_user():
    result = user_controller.save_user(request.json)
    if 'error' in result:
        return result.get('error'), 400
    return jsonify(result)

@app.route("/api/user", methods=['PUT'])
def update_user():
    pass

@app.route("/api/user", methods=['DELETE'])
def delete_user():
    pass

@app.route("/api/users",  methods=['GET'])
def get_all_users():
    pass

@app.route("/api/user/search/<name>",  methods=['GET'])
def get_user_by_name(name):
    pass

@app.route("/api/user/<id>",  methods=['GET'])
def get_user_by_id(id):
    user = user_controller.find_by_id(id)
    if not user:
        abort(404)
    return jsonify(user)