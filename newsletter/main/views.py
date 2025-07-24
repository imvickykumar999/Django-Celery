# from django.http import JsonResponse
from .tasks import test_celery_task
from django.shortcuts import render

def trigger_task(request):
    test_celery_task.delay()
    # return JsonResponse({'status': 'Task triggered'})
    return render(request, 'index.html')
