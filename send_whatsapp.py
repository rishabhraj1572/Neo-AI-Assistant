def send_whatsapp_message(to,msg):
    import requests

    api_key = 'YOUR_API'
    api_secret = 'YOUR_SECRET'

    recipient_phone_number = to

    url = 'https://messages-sandbox.nexmo.com/v1/messages'

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    }

    payload = {
        "from": "YOUR_NUMBER",
        "to": recipient_phone_number,
        "message_type": "text",
        "text": msg + '\n~Neo Assistant',
        "channel": "whatsapp"
    }

    response = requests.post(url, auth=(api_key, api_secret), headers=headers, json=payload)


