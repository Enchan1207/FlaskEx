#
# Flaskを使ってみる
#
from flask import Flask, render_template, request, make_response, jsonify
from datetime import datetime
import json

from Task import Task

# --
app = Flask(__name__)
tasks = []

# ルートはタスク一覧表示
@app.route('/')
def dumpTask():
    return make_response(jsonify([task.getObject() for task in tasks]), 200)

# Create
@app.route('/new', methods=['PUT'])
def addTask():
    if not request.headers.get("Content-Type") == 'application/json':
        error_message = {
            'error':'not supported Content-Type'
        }
        return make_response(jsonify(error_message), 400)

    return make_response(jsonify(request.json), 201)

if __name__ == "__main__":
    # ダミーをいくつか足して
    for i in range(5):
        tasks.append(Task("Dummy_" + str(i), "content_" + str(i)))

    # サーバ起動
    app.run(debug=True)