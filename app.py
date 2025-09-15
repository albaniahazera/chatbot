import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv

load_dotenv()
runningONPORT = os.getenv("PORT")
adminKey = os.getenv("KEY_CREATOR")
app = Flask(__name__)

@app.route('/')
def index():
    return "ChatBot Running!"

@app.route('/api/chatbot', methods=['POST'])
def chatBot():
    data = request.json
    message = data.get('message', '')

    if adminKey in message:
        response = "halo albania hazera, senang bertemu denganmu"
    elif "halo" or "hai" in message.lower():
        response = "Halo, apa yang bisa saya bantu ?"
    elif "siapa kamu ?" or "kamu ini apa ?" in message.lower():
        response = "saya C-Bot, dibuat oleh albania hazera dan hanya bisa diakses secara lokal."
    elif "tes" in message.lower():
        response = "ya ini test"
    else: 
        response = "maaf saya tidak tahu"

    
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=runningONPORT)