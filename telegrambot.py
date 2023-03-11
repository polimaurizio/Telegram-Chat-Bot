import requests
from dotenv import load_dotenv
import os

load_dotenv() #Load .env variable

def send_msg(text):
    token = os.getenv("TOKEN")
    chat_id = os.getenv("CHAT_ID")

    url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text
    
    #Send the message in telegram
    result = requests.get(url_req)
    
    #Print on terminal the result
    print(result.json())

send_msg("Hello my friend!")