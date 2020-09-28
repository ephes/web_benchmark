import time

from django.http import HttpResponse
from django.http import JsonResponse


def api(request):
    # time.sleep(1)
    payload = {"message": "Hello World!"}
    if "task_id" in request.GET:
        payload["task_id"] = request.GET["task_id"]
    return JsonResponse(payload)


async def async_api(request):
    # payload = {"message": "Hello World!"}
    # if "task_id" in request.GET:
    #    payload["task_id"] = request.GET["task_id"]
    # return JsonResponse(payload)
    return HttpResponse('{"message": "Hello World!"}')
