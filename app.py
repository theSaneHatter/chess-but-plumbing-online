print(f'{__name__} running!')
from flask import Flask, render_template, jsonify, request, abort
import time, random
from datetime import datetime
from flask_socketio import SocketIO, emit
import requests
import os
import sys
from pathlib import Path
from backend import lib as lib

messages = {"gid0":[{"timestamp":123,"uid":"user1","content":"message1"},
                    {"timestamp":67,"uid":"user2","content":"message2"}]}

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

@app.route('/get_gid', methods=['POST','GET'])
def get_gid():e
    global messages
    gid = lib.gen_gid(messages)
    messages[gid] = [{"timestamp":time.time(),"uid":"SERVER","content":f"gid >{gid}< initialized"}]
    print(f"@get_gid():user got gid:>{gid}<")
    ret = {"gid":gid}
    ret = jsonify(ret)
    return ret
           

@app.route('/get_messages',methods=['POST'])
def get_messages():
    global messages 
    
    data = request.get_json()
    toSend = []
    gid = data.get('gid')
    timestamp = data.get("timestamp")
    if not gid or not timestamp or not messages.get(gid):
        print(f"@send_message():user refranced non existant (or)[gid:{gid}, timestamp:{timestamp}]")
        return {"error":"Error sending messages: [gid, timestamp] may not exist"},404
    for i in messages.get(gid):
        print(f"@get_messages():i:>{i}<")
        if i["timestamp"] > timestamp:
            toSend.append(i)
    try:
        timestamp = int(timestamp)
    except ValueError:
        print(f"@get_messages():unable to convert timestamp:>{timestamp}< to int")
        return {"error":"invalud time"},400

    
    ret = toSend
    print(f"@get_messages():toSend:>{toSend}<")
  #  ret = {'date':time.time()}
    ret = jsonify(ret)

    return ret

@app.route('/send_message',methods=['POST'])
def send_message():
    global messages
    data = request.get_json()
    print(f"send_message() request:{data}")
    gid = data.get('gid')
    uid = data.get('uid')
    print(f"@debug:messages.get(>{gid}<):>{messages.get(gid)}<")
    if not messages.get(gid) or not gid or not uid:
        print(f"@send_message():user refranced non existant gid:{gid}")
        return {"error":"sending message:receved invalid (or)[gid, uid]"},404
    content = data.get("content")
    if not content:
        print(f"@send_message():user refranced non existant content:{content}")
        return {"error":"processing message: no/invalid content :("},404
    print(f"@send_message():[gid:>{gid}<,uid:>{uid}<,content:>{content}<]")
    messages[gid].append({"timestamp":time.time(),"uid":uid, "content":content})
    print(f"@send_message():messages:>{messages}<")

    ret = {"success":"true"}
    ret = jsonify(ret)
    return ret

        

if __name__ == '__main__':
    # lib.backup_logs()
    # config = lib.load_json()
    # port = config['port'] # to change port, edit config.json
    # socketio.run(app, host='0.0.0.0',port=port,debug=True, log_output=True)
    Flask.run(app, host='0.0.0.0',port=5000,debug=True, log_output=True)

