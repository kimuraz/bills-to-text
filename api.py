import base64
import os

from db import init_db, get_db
from flask import Flask, jsonify

app = Flask(__name__)
init_db()

@app.route('/', methods=['GET'])
def hello():
    return jsonify({ 'message': 'Hi there from bills-to-text api' })

@app.route('/api/nfs')
def get_nfs():
    pass

@app.route('/api/new-nf', methods=['POST'])
def new_nf():
    pass
