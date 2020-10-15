from django import forms

from .models import MataKuliahSaya

class MataKuliahForm(forms.ModelForm):
    nama = forms.CharField()
    dosen = forms.CharField()
    jumlahSKS = forms.IntegerField()
    semester = forms.CharField()
    ruangKelas = forms.CharField()

    class Meta:
        model = MataKuliahSaya
        fields = '__all__'