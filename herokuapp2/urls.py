from django.urls import path

from . import views

app_name = 'herokuapp2'

urlpatterns = [
    path('story1', views.page1, name='story1'),
]