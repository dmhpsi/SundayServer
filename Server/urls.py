from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api_login', views.api_login, name='api_login'),
    path('api_sync_info', views.api_sync_info, name='api_sync_info'),
    path('api_sync_contacts', views.api_sync_contacts, name='api_sync_contacts'),
]
