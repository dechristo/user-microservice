from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/api/status-check")
def status_check():
    return jsonify({'msg':'user microservice running...'})

@app.route("/api/user", methods=['POST'])
def add_user():
    pass

@app.route("/api/user", methods=['PUT'])
def update_user():
    pass

@app.route("/api/user", methods=['DELETE'])
def delete_user():
    pass

@app.route("/api/users",  methods=['GET'])
def get_all_users():
    pass

@app.route("/api/user/<name>",  methods=['GET'])
def get_user_by_name(name):
    pass

@app.route("/api/user/<id>",  methods=['GET'])
def get_user_by_id(id):
    pass