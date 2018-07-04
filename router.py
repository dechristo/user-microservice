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
        return jsonify(result), 400
    return jsonify(result)

@app.route("/api/user", methods=['PUT'])
def update_user():
    pass

@app.route("/api/user/<id>", methods=['DELETE'])
def delete_user(id):
    result = user_controller.delete_by_id(id)
    if 'error' in result or not result:
        return jsonify(result), 404
    return jsonify(result)

@app.route("/api/users",  methods=['GET'])
def get_all_users():
    pass

@app.route("/api/user",  methods=['GET'])
def get_user_by_filter_params():
    # name = request.args.get('name')
    # abort(404)
    pass

@app.route("/api/user/<id>",  methods=['GET'])
def get_user_by_id(id):
    user = user_controller.find_by_id(id)
    if 'error' in user or not user:
        abort(404)
    return jsonify(user)