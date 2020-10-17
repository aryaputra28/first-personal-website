from django.urls import path

from . import views

app_name = 'matakuliah'

urlpatterns = [
    path('ListMataKuliah', views.Utama, name='matakuliah_list'),
    path('FormMataKuliah',views.formMatkul, name='matakuliah_form'),
    path('<int:id>',views.matkulDetail),
    path('deleteMataKuliah/<str:id>', views.deleteMatkul,name="matakuliah_delete"),
    path('UpdateMataKuliah/<str:id>',views.updateMatkul,name="matakuliah_update")
]