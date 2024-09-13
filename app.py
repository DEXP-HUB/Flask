from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

# quotes = [
# {
# "id": 3,
# "author": "Rick Cook",
# "text": "Программирование сегодня — это гонка разработчиков программ, стремящихся писать программы с большей и лучшей идиотоустойчивостью, и вселенной, которая пытается создать больше отборных идиотов. Пока вселенная побеждает."
# },
# {
# "id": 5,
# "author": "Waldi Ravens",
# "text": "Программирование на С похоже на быстрые танцы на только что отполированном полу людей с острыми бритвами в руках."
# },
# {
# "id": 6,
# "author": "Mosher’s Law of Software Engineering",
# "text": "Не волнуйтесь, если что-то не работает. Если бы всё работало, вас бы уволили."
# },
# {
# "id": 8,
# "author": "Yoggi Berra",
# "text": "В теории, теория и практика неразделимы. На практике это не так."
# },
# ]

@app.route("/get", methods=['GET'])
def get_methods():
   connection = sqlite3.connect("store.db")
   cursor = connection.cursor()
   get = cursor.execute("SELECT * FROM quotes").fetchall
   return get
   

@app.route("/quotes")
def get_quotes():
   return quotes

@app.route("/quotes/<id>", methods=['POST'])
def edit_quote(id):
   quotes.append(id)
   print(quotes)

   
if __name__ == "__main__":
   app.run(debug=True)
