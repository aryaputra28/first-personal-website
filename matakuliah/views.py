from django.shortcuts import render,get_object_or_404, redirect
from django.http import HttpResponse, Http404
from .models import MataKuliahSaya
from .forms import MataKuliahForm

# Create your views here.
def Utama(request):
    matahkuliahs = MataKuliahSaya.objects.all()
    return render(request, 'matakuliah/matakuliah_list.html', {'matakuliahs':matahkuliahs} )

def formMatkul(request):
    form = MataKuliahForm()
    if request.method == 'POST':
        form = MataKuliahForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/ListMataKuliah')

    return render(request, 'matakuliah/matakuliah_forms.html',{'form':form})

def matkulDetail(request,id):
    matakuliah = MataKuliahSaya.objects.get(id=id)
    return render(request,'matakuliah/matakuliah_detail.html',{'matakuliah':matakuliah})

def deleteMatkul(request,id):
    item = MataKuliahSaya.objects.get(id=id)
    if request.method == 'POST' :
        item.delete()
        return redirect('/ListMataKuliah')

    return render(request, 'matakuliah/matakuliah_delete.html',{'item':item})

def updateMatkul(request,id):
    matakuliah = MataKuliahSaya.objects.get(id=id)
    form = MataKuliahForm(instance=matakuliah)
    if request.method == 'POST':
        form = MataKuliahForm(request.POST, instance=matakuliah)
        if form.is_valid():
            form.save()
            return redirect('/ListMataKuliah')
    context = {
        'form' :form
    }
    return render (request,'matakuliah/matakuliah_forms.html' ,context)
