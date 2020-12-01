from django.urls import path

from . import views

app_name = 'story82'

urlpatterns = [
    path('bookfinder2', views.utama, name='daftar_buku2'),
    path('getBooks',views.searchBook,name="getBooks"),
]