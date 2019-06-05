from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api_login', views.api_login, name='api_login'),
]
