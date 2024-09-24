import sqlite3


class DateBase:
    def __init__(self, path):
        self.path = path

    def get_quotes(self):
        with sqlite3.connect(self.path) as store:
            quotes = store.execute('SELECT * FROM quotes').fetchall()
            return quotes

    def delete_quote(self, id):
        with sqlite3.connect(self.path) as store:
            store.execute('DELETE FROM quotes WHERE id=?', (id,))
            store.commit()

    def get_quote(self, id):
        with sqlite3.connect(self.path) as store:
            quote = store.execute('SELECT * FROM quotes WHERE id = ?', (id,)).fetchone()
            return quote

    def update_quote(self, id, author, text):
        with sqlite3.connect(self.path) as store:
            store.execute('UPDATE quotes SET author = ?, text = ? WHERE id = ?', (author, text, id))
            store.commit()

    def add_quote(self, author, text):
        with sqlite3.connect(self.path) as store:
            store.execute('INSERT INTO quotes (author, text) VALUES(?, ?)', (author, text))
            store.commit()

