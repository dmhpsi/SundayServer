import json

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseForbidden, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User


def index(request):
    return render(request, "home.html")


@csrf_exempt
def api_login(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        try:
            username = body['username']
            password = body['password']
            user = User.objects.filter(username=username, password=password)
            if len(user) > 0:
                return JsonResponse({'result': 'ok'})
            else:
                return JsonResponse({'result': 'fail'})
        except KeyError:
            return JsonResponse({'result': 'fail'})
    return HttpResponseForbidden()
