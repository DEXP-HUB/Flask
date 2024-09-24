from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)


@app.route("/getquotes/", methods=['GET'])
def get_quotes():
    connection = sqlite3.connect('sqlite/store.db')
    quotes = connection.execute("""SELECT * FROM quotes""").fetchall()
    connection.close()
    return jsonify(quotes)


@app.route("/quote/<int:id>", methods=["GET"])
def get_quote(id):
    connection = sqlite3.connect('sqlite/store.db')
    quote = connection.execute("""SELECT * FROM quotes WHERE id = ?""", (id,)).fetchone()
    connection.close()
    return jsonify(id=quote[0], author=quote[1], quote=quote[2])


@app.route("/addquotes/", methods=['POST'])
def add_quote():
    date = request.json
    connection = sqlite3.connect('sqlite/store.db')
    connection.execute("""INSERT INTO quotes (author, text) VALUES (?, ?)""",
                       (date['author'], date['text']))
    connection.commit()
    connection.close()
    return jsonify(status=200)


@app.route("/updatequote/<int:id>", methods=['PUT'])
def update_quote(id):
    date = request.json
    connection = sqlite3.connect('sqlite/store.db')
    connection.execute("""UPDATE quotes SET author = ?, text = ? WHERE id = ?""",
                       (date['author'], date['text'], id))
    connection.commit()
    connection.close()
    return jsonify(status=200)


@app.route("/deletequote/<int:id>", methods=['DELETE'])
def delete_quote(id):
    connection = sqlite3.connect('sqlite/store.db')
    connection.execute("""DELETE FROM quotes WHERE id = ?""", (id,))
    connection.commit()
    connection.close()
    return jsonify(status=200)


if __name__ == "__main__":
    app.run(debug=True)
