from flask import Flask, jsonify, request
from sqlalchemy import update
from sqlalchemyDB.db_class import db, Quote



app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///store.db"
db.init_app(app)

    
@app.route("/getquotes/", methods=['GET'])
def get_quotes():
    get_quotes = db.session.execute(db.select(Quote.id, Quote.author, Quote.text)).fetchall()
    return [{"id": quote[0], "author": quote[1], "text": quote[2]} for quote in get_quotes]

@app.route("/quote/<int:id>", methods=["GET"])
def get_quote(id):
    get_quote = db.session.get(Quote, id)
    return jsonify(id = get_quote.id, author = get_quote.author, quote = get_quote.text)


@app.route("/addquotes/", methods=['POST'])
def add_quote():
    quote = request.json
    quote = Quote(author=quote['author'], text=quote['quote'])
    db.session.add(quote)
    db.session.commit()
    return jsonify(status=200)


@app.route("/updatequote/<int:id>", methods=['PUT'])
def update_quote(id):
    get_request = request.json
    get_quote = db.session.get(Quote, id)
    get_quote.author = get_request['author']
    get_quotes.text = get_request['quote']
    db.session.commit()
    return jsonify(status = 200)
    


@app.route("/deletequote/<int:id>", methods=['DELETE'])
def delete_quote(id):
    get_quote = db.session.get(Quote, id)
    db.session.delete(get_quote)
    db.session.commit()
    return jsonify(status=200)


if __name__ == "__main__":
    app.run(debug=True)
    
