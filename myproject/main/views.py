from django.http import JsonResponse
from .tasks import test_celery_task

def trigger_task(request):
    test_celery_task.delay()
    return JsonResponse({'status': 'Task triggered'})
