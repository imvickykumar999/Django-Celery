# from celery import shared_task
# import time

# @shared_task
# def test_celery_task():
#     print("Task started")
#     time.sleep(5)
#     print("Task completed")
#     return "Done"

  GNU nano 8.1                                                                                                                   tasks.py                                                                                                                             
from celery import shared_task
import time
import requests

def send_telegram_message(message):
    chat_ids = ['5721393154']  # Add more if needed

    bot_token = '6165663083:AAG9RI431DBbMKxGETvDBjmSoeX2wck8BmI'
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"

    for chat_id in chat_ids:
        payload = {
            "chat_id": chat_id,
            "text": message,
            "parse_mode": "Markdown"
        }
        response = requests.post(url, data=payload)

        if response.status_code == 200:
            print(f"Message sent to chat_id: {chat_id}")
        else:
            print(f"Failed to send message to chat_id: {chat_id}, Status Code: {response.status_code}")

@shared_task
def test_celery_task():
    print("Checking Minecraft server status...")

    try:
        # Fetch the Minecraft Bedrock server status
        url = "https://api.mcstatus.io/v2/status/bedrock/bedrock.imvickykumar999.online:5625"
        response = requests.get(url, timeout=10)
        data = response.json()

        is_online = data.get("online", False)
        ip = data.get("ip_address", "Unknown")
        port = data.get("port", "Unknown")

        if is_online:
            message = f"✅ Your Minecraft server is *ONLINE*\nIP: `{ip}`\nPort: `{port}`"
        else:
            message = f"❌ Your Minecraft server is *OFFLINE*\nIP: `{ip}`\nPort: `{port}`"

        # Send the message
        send_telegram_message(message)
    except Exception as e:
        send_telegram_message(f"⚠️ Failed to fetch server status.\nError: `{str(e)}`")
        print(f"Error: {e}")

    return "Status check completed"

