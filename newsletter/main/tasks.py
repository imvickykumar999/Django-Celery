from celery import shared_task
import requests
from .utils import send_telegram_message  # Import the function to send messages from utils

@shared_task
def test_celery_task():
    """
    This task checks the Minecraft server status and sends an update to Telegram.
    It runs periodically to check if the server is online or offline.
    """
    print("Checking Minecraft server status...")

    try:
        # Fetch the Minecraft Bedrock server status (adjust URL as needed)
        url = "https://api.mcstatus.io/v2/status/bedrock/bedrock.imvickykumar999.online:5625"
        response = requests.get(url, timeout=10)
        data = response.json()

        # Extract server status details
        is_online = data.get("online", False)
        ip = data.get("ip_address", "Unknown")
        port = data.get("port", "Unknown")

        if is_online:
            # Construct message if the server is online
            message = f"✅ Your Minecraft server is *ONLINE*\nIP: `{ip}`\nPort: `{port}`"
        else:
            # Construct message if the server is offline
            message = f"❌ Your Minecraft server is *OFFLINE*\nIP: `{ip}`\nPort: `{port}`"

        # Send or update the message
        send_telegram_message(message, update_message=True)

    except Exception as e:
        # If an error occurs while fetching the status, send an error message
        send_telegram_message(f"⚠️ Failed to fetch server status.\nError: `{str(e)}`")
        print(f"Error: {e}")

    return "Status check completed"
