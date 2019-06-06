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
            print(body)
            if len(user) > 0:
                return JsonResponse({'result': 'ok'})
            else:
                return JsonResponse({'result': 'fail'})
        except KeyError:
            return JsonResponse({'result': 'fail'})
    return HttpResponseForbidden()


@csrf_exempt
def api_sync_info(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        try:
            username = body['username']
            password = body['password']
            data = body['data']
            timestamp = int(body['timestamp'])
            user = User.objects.filter(username=username, password=password)
            print(body)
            if len(user) > 0:
                xuser = user[0]
                if xuser.info_time < timestamp:
                    xuser.info = data
                    xuser.info_time = timestamp
                    xuser.save()
                return JsonResponse({'result': 'ok', 'data': xuser.info, 'timestamp': xuser.info_time})
            else:
                return JsonResponse({'result': 'fail'})
        except KeyError:
            return JsonResponse({'result': 'fail'})
    return HttpResponseForbidden()


@csrf_exempt
def api_sync_contacts(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        try:
            username = body['username']
            password = body['password']
            data = body['data']
            timestamp = int(body['timestamp'])
            user = User.objects.filter(username=username, password=password)
            print(body)
            if len(user) > 0:
                xuser = user[0]
                if xuser.contacts_time < timestamp:
                    xuser.contacts = data
                    xuser.contacts_time = timestamp
                    xuser.save()
                return JsonResponse({'result': 'ok', 'data': xuser.contacts, 'timestamp': xuser.contacts_time})
            else:
                return JsonResponse({'result': 'fail'})
        except KeyError:
            return JsonResponse({'result': 'fail'})
    return HttpResponseForbidden()
