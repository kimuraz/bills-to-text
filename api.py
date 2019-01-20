import base64
import os
import sqlite3

from flask import (Flask, jsonify, request)

from db import init_db, get_db
from nf_read_search import get_bill_info

app = Flask(__name__)
init_db()

@app.route('/', methods=['GET'])
def hello():
    return jsonify({ 'message': 'Hi there from bills-to-text api' })

@app.route('/api/nfs', methods=['GET', 'DELETE'])
def get_nfs():
    nfs = ()
    cur = get_db().execute('select * from nfs')
    for nf in cur.fetchall():
        nfs.append(nf)
    cur.close()
    return jsonify(nfs)

@app.route('/api/new-nf', methods=['POST'])
def new_nf():
    nf = request.get_json()
    parsed_infos = get_bill_info(nf['img'])
    query = 'INSERT INTO nfs (name, description, img, emit_date, total) '\
            'VALUES ({},{},{},{},{})'.format(
                nf['name'], nf['description'], nf['img'],
                parsed_infos['date'], parsed_infos['total']
            )
    cur = get_db().cursor()
    cur.execute(query)
    cur.close()

    return jsonify(parsed_infos) 
