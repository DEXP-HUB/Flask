from flask import Flask, jsonify, request
from sqlite.class_db import DateBase

app = Flask(__name__)


@app.route("/getquotes/", methods=['GET'])
def get_quotes():
    execute = DateBase("sqlite//store.db")
    get_quotes = execute.get_quotes()
    return jsonify(get_quotes)


@app.route("/quote/<int:id>", methods=["GET"])
def get_quote(id):
    execute = DateBase("sqlite//store.db")
    quote = execute.get_quote(id)
    return jsonify(id=quote[0], author=quote[1], quote=quote[2])


@app.route("/addquotes/", methods=['POST'])
def add_quote():
    date = request.json
    execute = DateBase("sqlite//store.db")
    quote = execute.add_quote(date["author"], date["quote"])
    return jsonify(status=200)


@app.route("/updatequote/<int:id>", methods=['PUT'])
def update_quote(id):
    date = request.json
    execute = DateBase("sqlite//store.db")
    execute.update_quote(id, date['author'], date['text'])
    return jsonify(status=200)


@app.route("/deletequote/<int:id>", methods=['DELETE'])
def delete_quote(id):
    execute = DateBase("sqlite//store.db")
    execute.delete_quote(id)
    return jsonify(status=200)


if __name__ == "__main__":
    app.run(debug=True)
