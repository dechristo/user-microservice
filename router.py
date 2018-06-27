import _mysql
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    db=_mysql.connect("localhost","root","verysecure","userms")
    return jsonify({'msg':'user microservice running...'})