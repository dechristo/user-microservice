from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def hello():
    return jsonify({'msg':'user microservice running...'})