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

    if "halo" in message.lower():
        response = "Halo, apa yang bisa saya bantu?", "1. Mengembalikan pesan", "2. Siapa kamu ?", '''PILIH 1-2'''
    elif "1" in message:
        response = f"Pesan kamu: [{message}]"
    elif "2" in message:
        response = "saya C-Bot, dibuat oleh albania hazera dan hanya bisa diakses dijaringan lokal."
    elif "tes" in message.lower():
        response = "ya ini test"
    elif adminKey in message:
        response = "halo albania hazera, senang bertemu denganmu"
    else: 
        response = "maaf saya tidak tahu"

    
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=runningONPORT)