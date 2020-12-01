from django.test import TestCase
from django.test import Client
from django.urls import resolve
from django.http import HttpRequest, response

from .views import *

class test_path(TestCase):
    def test_path(self):
        response = Client().get('/bookfinder2',{},True)
        self.assertEqual(response.status_code,200)

class text_input(TestCase):
    def test_textHTML(self):
        response = Client().get('/bookfinder2')
        html = response.content.decode('utf-8')
        self.assertIn("Book Finder",html)
        self.assertIn("Nama Buku",html)

class test_template(TestCase):
    def test_template1(self):
        response = Client().get('/bookfinder2')
        self.assertTemplateUsed(response,'base.html')