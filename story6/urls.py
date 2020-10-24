from django.urls import path

from . import views

app_name = 'story6'

urlpatterns = [
    path('daftar/', views.daftar, name='daftar'),
    path('hapus/', views.hapus, name="hapus"),
    path('ListKegiatan', views.Utama, name='kegiatan_list'),
]