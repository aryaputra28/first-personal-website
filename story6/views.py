from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def Utama(request):
    kegiatans = KegiatanSaya.objects.all()
    participants = Participant.objects.all()
    keg_par = []
    for kegiatan in kegiatans:
        kegiatan_partic = []
        for participant in participants:
            if (str(participant.kegiatan) == str(kegiatan)):
                kegiatan_partic.append(participant)
        keg_par.append((kegiatan,kegiatan_partic))
    
    context = {
        "hasil_list" : keg_par
    }
    return render(request, 'story6/kegiatan_list.html', context )

def daftar(request):
    id_kegiatan = request.POST.get('id_kegiatan', None)
    name_participant = request.POST.get('name_participant',None)
    nama_kegiatan = request.POST.get('nama_kegiatan', None)

    if (id_kegiatan and name_participant) :
        Participant.objects.create(name=name_participant, kegiatan=KegiatanSaya.objects.get(id = id_kegiatan))
    else:
        KegiatanSaya.objects.create(NamaKegiatan=nama_kegiatan)

    return redirect('/ListKegiatan')

def hapus(request):
    id_participant = request.POST.get('id_participant', None)
    participant = Participant.objects.get(id = id_participant)
    participant.delete()
    # return render(request, 'story6/ListKegiatan.html')
    return redirect('/ListKegiatan')
