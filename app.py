import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from flask import Flask, request, jsonify

# Data pelatihan: pasangan (kalimat, niat)
training_data = [
    ("halo", "salam"),
    ("hai", "salam"),
    ("hello", "salam"),
    ("siapa namamu", "identitas"),
    ("namamu siapa", "identitas"),
    ("apa yang bisa kamu lakukan", "kemampuan"),
    ("kamu bisa apa", "kemampuan"),
    ("berapa umurmu", "umur"),
    ("umurmu berapa", "umur")
]

# Memisahkan kalimat (X) dan niat (y)
sentences = [data[0] for data in training_data]
intents = [data[1] for data in training_data]

# Membuat pipeline yang menggabungkan vektorisasi teks dan klasifikasi
model = make_pipeline(TfidfVectorizer(), MultinomialNB())

# Melatih model dengan data pelatihan
model.fit(sentences, intents)

def predict_intent(text):
    return model.predict([text])[0]

def get_response(intent):
    if intent == "salam":
        return "Halo! Ada yang bisa saya bantu?"
    elif intent == "identitas":
        return "Saya adalah chatbot yang dibuat untuk membantu Anda."
    elif intent == "kemampuan":
        return "Saya bisa memproses teks dan memberikan respons berdasarkan niat."
    elif intent == "umur":
        return "Saya tidak memiliki umur, saya hanyalah kode."
    else:
        return "Maaf, saya tidak mengerti."

app = Flask(__name__)

@app.route('/')
def main():
    return 'CHATBOT Running'

@app.route('/api/chatbot', methods=['POST'])
def chatBot():
    data = request.json
    message = data.get('message', '')

    # Menggunakan model untuk memprediksi niat dari pesan pengguna
    intent = predict_intent(message)
    
    # Mendapatkan respons berdasarkan niat yang diprediksi
    response_text = get_response(intent)
    
    return jsonify({"response": response_text})

if __name__ == '__main__':
    # Jangan gunakan di produksi
    app.run(host='0.0.0.0', port=5000)