from django.test import TestCase
from django.test import Client
from django.urls import resolve, reverse
from django.http import HttpRequest, response
from .views import *

class test_path(TestCase):
    def test_path(self):
        response = Client().get('/login',{},True)
        self.assertEqual(response.status_code,200)
    def test_path2(self):
        response = Client().get('/register',{},True)
        self.assertEqual(response.status_code,200)
    def test_path3(self):
        response = Client().get('/logout',{},True)
        self.assertEqual(response.status_code,200)

class text_input(TestCase):
    def test_textHTMLLogin(self):
        response = Client().get('/login')
        html = response.content.decode('utf-8')
        self.assertIn("username", html)
        self.assertIn('password',html)
    def test_textHTMLDaftar(self):
        response = Client().get('/register')
        html = response.content.decode('utf-8')
        self.assertIn("username",html)
        self.assertIn("password", html)
        self.assertIn("Email address", html)

class test_urls(TestCase):
    def setUp(self):
        self.login = reverse("story9:login")
        self.register = reverse("story9:register")
        self.logout = reverse("story9:logout")
    
    def test_login_use_right_function(self):
        found = resolve(self.login)
        self.assertEqual(found.func, loginAkun)

    def test_register_use_right_function(self):
        found = resolve(self.register)
        self.assertEqual(found.func, register)

    def test_logout_use_right_function(self):
        found = resolve(self.logout)
        self.assertEqual(found.func, logoutAkun)

class UserCreationFormTest(TestCase):
    def test_form(self):
        data = {
            'username': 'testuser21',
            'email':'test@gmail.com',
            'password1': 'testingpass213',
            'password2': 'testingpass213',
        }
        form = UserCreationForm(data)
        self.assertTrue(form.is_valid())
