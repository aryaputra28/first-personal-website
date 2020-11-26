from django.test import TestCase
from django.test import Client
from django.urls import resolve
from django.http import HttpRequest, response

from story6.models import *
import story6.views 

class DetailPageUnitTest(TestCase) :
    def test_story6_url_is_exist (self) :
        response = Client().get('/ListKegiatan')
        self.assertEqual(response.status_code, 200)
        
        response = Client().get('/daftar')
        self.assertEqual(response.status_code, 301)

        response = Client().get('/hapus')
        self.assertEqual(response.status_code, 301)

    def test_story6_membuat_model_kegiatan (self) :
        kegiatan = KegiatanSaya.objects.create(NamaKegiatan="nama kegiatan")

        count = KegiatanSaya.objects.all().count()
        self.assertEqual(count, 1)

    def test_story6_membuat_model_participant (self):
        kegiatan = KegiatanSaya.objects.create(NamaKegiatan="Mantap Jiwa", Deskripsi="x")
        participant = Participant.objects.create(name="arya",kegiatan=kegiatan)
        self.assertEquals(str(participant),"Mantap Jiwax dan arya")

    def test_story6_penggunaan_template(self):
        kegiatan = KegiatanSaya.objects.create(NamaKegiatan="Nama Kegiatan")
        participant = Participant.objects.create(name="arya",kegiatan=kegiatan)

        response = Client().get('/ListKegiatan')
        self.assertTemplateUsed(response,"base.html")
    
    def test_story6_menyimpan_post_kegiatanbaeru(self):
        response = Client().post('/daftar/', data={
            "nama_kegiatan" : "event_test",
            "deskripsi_kegiatan" : "bingung"
        })
        count = KegiatanSaya.objects.all().count()
        self.assertEqual(count,1)
        self.assertEqual(response.status_code, 302)

    def test_story6_menyimpan_POST_participantbaru(self):
        kegiatan = KegiatanSaya.objects.create(NamaKegiatan="kegiatan_test")
        response = Client().post('/daftar/',data= {
            "id_kegiatan" : "1",
            "name_participant" : "Arya"
        })

        count = Participant.objects.all().count()
        self.assertEqual(count,1)
        self.assertEqual(response.status_code,302)

    def test_menambahdata_dan_menghapusdata(self):
        kegiatan = KegiatanSaya.objects.create(NamaKegiatan="kegiatan_test")
        response = Client().post('/daftar/', data= {
            "id_kegiatan" : "1",
            "name_participant" : "Arya"
        })
        count = Participant.objects.all().count()
        self.assertEqual(count,1)
        self.assertEqual(response.status_code,302)

        response = Client().post('/hapus/',data= {
            "id_participant" : 1,
        })
        count = Participant.objects.all().count()
        self.assertEqual(count,0)
