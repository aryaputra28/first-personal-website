from django.urls import path

from . import views

app_name = 'herokuapp'

urlpatterns = [
    path('', views.page1),
    path('portofolio',views.page2),
    path('story1',views.page3)
]