#
# Flaskを使ってみる
#
from flask import Flask, render_template, request, make_response, jsonify
from datetime import datetime
import json

from Task import Task
from jsonDecorator import contentType

# --
app = Flask(__name__)
tasks = []

# ルートはタスク一覧表示
@app.route('/')
def dumpTask():
    return make_response(jsonify([task.getObject() for task in tasks]), 200)

# Create
@app.route('/create', methods = ['PUT'])
@contentType('application/json')
def createTask():
    queryJson = request.json
    # titleとcontentは必須パラメータ
    if not queryJson.keys() >= {"title", "content"}:
        return make_response(jsonify("{'error': 'Invalid parameter'}"), 400)
    
    newTask = Task(queryJson['title'], queryJson['content'], float(queryJson.get('limit')))
    tasks.append(newTask)
    return make_response(newTask.getObject(), 201)

# Read
@app.route('/get/<string:taskID>')
def getTask(taskID = None):
    targets = list(filter(lambda task: task.taskID == taskID, tasks))
    if len(targets) == 1:
        return make_response(jsonify(targets[0].getObject()), 201)
    else:
        return make_response(jsonify("{'error': 'Not Found'}"), 404)
    
# Update
@app.route('/update/<string:taskID>', methods = ['PUT'])
@contentType('application/json')
def updateTask(taskID = None):
    queryJson = request.json
    target = None

    for task in tasks:
        if task.taskID != taskID:
            continue

        target = task
        # 変更可能なキー
        validKeys = ["title", "content", "limit"]
        for validKey in validKeys:
            newValue = queryJson.get(validKey)
            if newValue is not None:
                setattr(task, validKey, newValue)
    
    if target is not None:
        return make_response(jsonify(target.getObject()), 201)
    else:
        return make_response(jsonify("{'error': 'Not Found'}"), 404)

# Delete
@app.route('/delete/<string:taskID>', methods = ['DELETE'])
def deleteTask(taskID = None):

    return make_response(jsonify({'result': "Deleted."}), 200)

if __name__ == "__main__":

    # サーバ起動
    app.run(debug=True)