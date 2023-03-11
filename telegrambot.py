import requests
from dotenv import load_dotenv
import os

load_dotenv() #Carica variabili fine .env

def send_msg(text):
    token = os.getenv("TOKEN")
    chat_id = os.getenv("CHAT_ID")

    url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text
    result = requests.get(url_req)
    
    print(result.json())

send_msg("Messaggio automatico python")