import requests
import os

url = 'https://ndu.pythonanywhere.com/webhook'

TOKEN = os.environ["TOKEN"]

payload = {
    "url":url
}

r = requests.get(f"https://api.telegram.org/bot{TOKEN}/setWebhook", params=payload)
r = requests.get(f"https://api.telegram.org/bot{TOKEN}/GetWebhookInfo", params=payload)



print(r.json())