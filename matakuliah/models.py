from django.db import models

# Create your models here.
class MataKuliahSaya(models.Model):
    nama = models.CharField(max_length = 100)
    dosen = models.CharField(max_length = 100)
    jumlahSKS = models.PositiveIntegerField()
    semester = models.CharField(max_length = 100)
    ruangKelas = models.CharField(max_length= 100)
    deskripsi = models.CharField(max_length = 500)

    def __str__(self):
        return self.nama