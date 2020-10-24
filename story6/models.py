from django.db import models

# Create your models here.
class KegiatanSaya(models.Model):
    NamaKegiatan = models.CharField(max_length=500)
    Deskripsi = models.TextField(max_length=500)
    def __str__(self):
        return self.NamaKegiatan
    def __str__(self):
        return self.Deskripsi   

class Participant(models.Model):
    name = models.CharField(max_length = 200)
    kegiatan = models.ForeignKey(KegiatanSaya, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.kegiatan) + " dan " + self.name