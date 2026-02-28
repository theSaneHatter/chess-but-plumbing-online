print(f'{__name__} running!')
from flask import Flask, render_template, jsonify, request, abort
import time, random
from datetime import datetime
from flask_socketio import SocketIO, emit
import requests
import os
import sys
from pathlib import Path
# from backend import lib as lib

messages = {"uid1":[123,"message1"]}

app = Flask(__name__,
            template_folder="frontend/templates/",
            static_folder="frontend",
            static_url_path="/frontend"
            )

socketio = SocketIO(app)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/hello',methods=['POST','GET'])
def hello():
    return jsonify({'response':'hello'})

@app.route('/request_messages',methods=['POST'])
def message_handler():
    global messages 
    
    data = request.get_json()
    ret = messages
  #  ret = {'date':time.time()}
    ret = jsonify(ret)

    print(f'the user sent a message:{data}')
    return ret

@app.route('/send_message',methods=['POST'])
def send_message():
    global messages
    data = request.get_json()
    print(f"send_message() request:{data}")
    uid = data.get('uid')
    if not messages.get(uid):
        print(f"@send_message():user refranced non existant uid:{uid}")
        return 400
    content = data.get("content")
    if not content:
        print(f"@send_message():user refranced non existant content:{content}")
        return 400
    print(f"@send_message():uid:>{uid}<,content:>{content}<")
    messages[uid].append([time.time(), content])

    ret = {"success":"true"}
    ret = jsonify(ret)
    return ret


        

if __name__ == '__main__':
    # lib.backup_logs()
    # config = lib.load_json()
    # port = config['port'] # to change port, edit config.json
    # socketio.run(app, host='0.0.0.0',port=port,debug=True, log_output=True)
    Flask.run(app, host='0.0.0.0',port=5000,debug=True, log_output=True)

