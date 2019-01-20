import sqlite3

from flask import Flask, g

DATABASE = './imgs/nfs.db'

app = Flask(__name__)

def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('./extras/nfs.sql', mode='r') as sql:
            db.cursor().executescript(sql.read())
        db.commit()

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
