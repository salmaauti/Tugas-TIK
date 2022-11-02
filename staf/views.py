from django.shortcuts import render, redirect
from staf.models import Staf
from staf.forms import FormStaf
from django.contrib import messages
# Create your views here.

def hapus_staf(request, id_staf):
    staf = Staf.objects.filter(id=id_staf)
    staf.delete()
    if request.method == "POST":
        staf.hapus()

    return redirect('staf')


def ubah_staf(request, id_staf):
    staf = Staf.objects.get(id=id_staf)
    template = 'ubah-staf.html'
    if request.POST:
        form = FormStaf(request.POST, instance=staf)
        if form.is_valid():
            form.save()
            messages.success(request, "Data berhasil diperbaharui") 
            return redirect('ubah_staf', id_staf=id_staf)

    else:
        form = FormStaf(instance=staf)
        context = {
            'form': form,
            'staf': staf,
        }
        return render(request, template, context)

def staf(request):
    context = {
        'educator': Staf.objects.all()
        
    }
    return render(request,"indexs.html", context)

def tambah_staf(request):
    if request.POST:
        form = FormStaf(request.POST)
        if form.is_valid():
            form.save()
            form = FormStaf()
            pesan = "Data berhasil disimpan"
            context = {
                'form': form,
                'pesan': pesan,
            }
            return render(request, 'tambah-staf.html', context)
    
    else:
        form = FormStaf()
    
        context = {
            'form': form,

        }
    return render(request, 'tambah-staf.html', context)
