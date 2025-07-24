import requests
from .models import TelegramMessage

BOT_TOKEN = '6165xxxxx:xxxxxxxxxxxxxxxxxxxxxxxxxxxxrTjS60'

SEND_MESSAGE_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
EDIT_MESSAGE_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/editMessageText"

CHAT_IDS = ['5721393154']


def send_telegram_message(message, update_message=False, is_error=False):
    """
    Sends or updates a message based on the flag.
    """
    for chat_id in CHAT_IDS:
        try:
            if update_message:
                # Check if there's a previous message saved for this chat
                existing = TelegramMessage.objects.filter(chat_id=chat_id).first()
                if existing:
                    if existing.last_message == message:
                        print(f"⏭️ Skipped update: message is unchanged for chat_id {chat_id}")
                        return  # Avoid Telegram's 400 error

                    payload = {
                        "chat_id": chat_id,
                        "message_id": existing.message_id,
                        "text": message,
                        "parse_mode": "Markdown"
                    }
                    response = requests.post(EDIT_MESSAGE_URL, data=payload)

                    if response.status_code == 200:
                        existing.last_message = message
                        existing.save(update_fields=['last_message'])
                        print(f"✅ Message updated for chat_id: {chat_id}")
                    else:
                        print(f"❌ Failed to update message for chat_id: {chat_id}")
                        try:
                            print("📬 Telegram error response:", response.json())
                        except Exception:
                            print("⚠️ Could not parse error response.")
                else:
                    print(f"ℹ️ No previous message, sending new to chat_id: {chat_id}")
                    send_new_message(chat_id, message, is_error)
            else:
                send_new_message(chat_id, message, is_error)

        except Exception as e:
            print(f"🔥 Error sending/updating message for chat_id {chat_id}: {e}")
            if not is_error:
                # This is where you send an error message in case of unexpected errors
                send_new_message(chat_id, f"⚠️ An unexpected error occurred: {str(e)}", is_error=True)


def send_new_message(chat_id, message, is_error=False):
    """
    Sends a new Telegram message and saves its message_id for future updates.
    """
    payload = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "Markdown"
    }

    response = requests.post(SEND_MESSAGE_URL, data=payload)

    if response.status_code == 200:
        try:
            data = response.json()
            message_id = data["result"]["message_id"]
            TelegramMessage.objects.update_or_create(
                chat_id=chat_id,
                defaults={"message_id": message_id, "last_message": message}
            )
            print(f"📤 Message sent to chat_id: {chat_id}, saved message_id: {message_id}")
        except Exception as e:
            print(f"⚠️ Message sent but failed to save message_id: {e}")
    else:
        print(f"❌ Failed to send new message to chat_id: {chat_id}, Status Code: {response.status_code}")
        try:
            print("📬 Telegram error response:", response.json())
        except Exception:
            print("⚠️ Could not parse error response.")
