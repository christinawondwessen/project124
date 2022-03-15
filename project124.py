from numpy import False_
from flask import Flask, jsonify, request

@app.route("/add-data",methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"please provide data"
        },400)