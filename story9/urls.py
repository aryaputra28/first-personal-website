from django.urls import path

from . import views

app_name = 'story9'

urlpatterns = [
    path('login',views.loginAkun,name="login"),
    path('register',views.register, name="register"),
    path('logout',views.logoutAkun, name="logout")
]