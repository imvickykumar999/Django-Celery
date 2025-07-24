from django.db import models

class TelegramMessage(models.Model):
    chat_id = models.CharField(max_length=255, unique=True)
    message_id = models.IntegerField()
    last_message = models.TextField(null=True, blank=True)  # <-- Add this

    def __str__(self):
        return f"Message {self.message_id} in Chat {self.chat_id}"

