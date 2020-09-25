from django.urls import path

from . import views

app_name = 'herokuapp'

urlpatterns = [
    path('', views.page1),
    path('Photography',views.page2)
]