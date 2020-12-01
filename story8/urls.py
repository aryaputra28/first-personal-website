from django.urls import path

from . import views

app_name = 'story8'

urlpatterns = [
    path('bookfinder', views.utama, name='daftar_buku'),
]