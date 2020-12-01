from django.test import TestCase
from django.test import Client
from django.urls import resolve
from django.http import HttpRequest, response

from .views import *

class test_path(TestCase):
    def test_path(self):
        response = Client().get('/',{},True)
        self.assertEquals(response.status_code,200)
    
class testInput(TestCase):
    def test_textHTML(self):
        response = Client().get('/')
        html = response.content.decode('utf-8')
        self.assertIn('Aryaputra Athallah',html)
        self.assertIn('About Me',html)
    def test_textHTML(self):
        response = Client().get('/portofolio')
        html = response.content.decode('utf-8')
        self.assertIn('Mobile Development UI/UX',html)
        self.assertIn('Photography',html)

class testFuncition(TestCase):
    def test_url_using_func(self):
        found = resolve('/')
        self.assertEqual(found.func, page1)
    def test_url_using_func2(self):
        found = resolve('/portofolio')
        self.assertEqual(found.func,page2)

class test_template(TestCase):
    def test_template1(self):
        response = Client().get('/')
        self.assertTemplateUsed(response,'base.html')
    def test_template2(self):
        response = Client().get('/portofolio')
        self.assertTemplateUsed(response,'base.html')