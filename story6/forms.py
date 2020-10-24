from django import forms
from .models import *

class KegiatanForm(forms.ModelForm):
    NamaKegiatan = forms.CharField()
    Deskripsi = forms.Textarea()
    class Meta:
        model = KegiatanSaya
        fields = '__all__'

class ParticipantForm(forms.ModelForm):
    class Meta:
        model =  Participant
        fields = '__all__'