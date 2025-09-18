import requests, os

osType = os.name
api_url = "http://10.152.226.12:5000/api/chatbot"

def chat_with_bot():
    if osType == "nt":
        os.system('cls')
    else:
        os.system('clear')
    print("Selamat datang di Chatbot! Ketik 'keluar' untuk mengakhiri.\n")
    
    while True:
        user_input = input("Anda: ")
        if user_input.lower() == 'keluar':
            break

        payload = {"message": user_input}
        
        try:
            response = requests.post(api_url, json=payload)
            response.raise_for_status()
            
            bot_response = response.json().get('response')
            print(f"Chatbot: {bot_response}")
            
        except requests.exceptions.RequestException as e:
            print(f"Terjadi kesalahan: {e}")
            break

if __name__ == "__main__":
    chat_with_bot()