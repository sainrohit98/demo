from email.mime import application
from flask import Flask,request
import json


app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello'

@app.route('/github',methods=['POST'])
def webhook():
    if request.headers['Content-Type'] == 'application/json':
        my_Info = json.dumps(request.json)
    return my_Info





if __name__ ==  "__main__":
    app.run(debug = True,port = 5000)