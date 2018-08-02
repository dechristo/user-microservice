from flask import Flask, jsonify, request, abort, session
from src.controllers.user_controller import UserController


app = Flask(__name__)
app.secret_key = "super secret key"
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

@app.route("/api/user/<id>", methods=['PUT'])
def update_user(id):
   result = user_controller.update_user(id, request.json)
   if 'error' in result:
       return jsonify(result), 400
   return jsonify(result)

@app.route("/api/user/<id>", methods=['DELETE'])
def delete_user(id):
    result = user_controller.delete_by_id(id)
    if 'error' in result or not result:
        return jsonify(result), 404
    return jsonify(result)

@app.route("/api/users",  methods=['GET'])
def get_all_users():
    if session.get('is_logged'):
        result = user_controller.get_all()
        if 'error' in result or not result:
            return jsonify(result), 404
        return jsonify(result)
    return jsonify('not logged in'), 403

@app.route("/api/user",  methods=['GET'])
def get_user_by_filter_params():
    name = request.args.get('name')
    if not name:
         abort(404)
    result = user_controller.find_by_name(name)
    if not result or not result.get('data'):
       return abort(404)
    return jsonify(result)

@app.route("/api/user/<id>",  methods=['GET'])
def get_user_by_id(id):
    user = user_controller.find_by_id(id)
    if 'error' in user or not user:
        abort(404)
    return jsonify(user)

@app.route("/api/user/address/<zip_code>", methods=['GET'])
def get_address_by_zip_code(zip_code):
    result = user_controller.get_address_by_zip_code(zip_code)
    return jsonify(result) if result else abort(404)

@app.route("/api/login", methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    if not username or not password:
        return abort(400)
    is_logged_in = user_controller.login(username, password)
    if 'error' in is_logged_in:
        return jsonify(is_logged_in,), 404
    session['is_logged'] = True
    return jsonify(is_logged_in,)