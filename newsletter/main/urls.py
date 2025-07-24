from django.urls import path
from .views import trigger_task
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', trigger_task),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
