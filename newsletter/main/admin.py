from django.contrib import admin
from .models import TelegramMessage

class TelegramMessageAdmin(admin.ModelAdmin):
    list_display = ('chat_id', 'message_id', 'last_message')
    search_fields = ('chat_id', 'message_id')
    list_filter = ('chat_id',)
    list_editable = ('last_message',)
    
    fieldsets = (
        (None, {
            'fields': ('chat_id', 'message_id', 'last_message')
        }),
    )

admin.site.register(TelegramMessage, TelegramMessageAdmin)
