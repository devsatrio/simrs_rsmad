from django.shortcuts import render,redirect
from .tables import KaryawanTable
from .models import Karyawan
from .filters import KaryawanFilter
from .forms import KaryawanForm
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.db.models import ProtectedError
from django_tables2 import RequestConfig

#========================================================================================================================
def index(request):
    f = KaryawanFilter(request.GET, queryset=Karyawan.objects.all())
    table_karyawan = KaryawanTable(f.qs)
    context = {
        'tabel_karyawan':table_karyawan,
        'filter':f,
    }
    return render(request,'karyawan/index.html',context)

#========================================================================================================================
def create(request):
    form = KaryawanForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Data Berhasil Disimpan')
        return redirect('karyawan:index')
    
    context={
        'form':form
    }
    return render(request,'karyawan/create.html',context)

#========================================================================================================================
def edit(request,id):
    obj = get_object_or_404(Karyawan, id = id)
    form = KaryawanForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        messages.success(request, 'Data Berhasil Diedit')
        return redirect('karyawan:index')
    
    context={
        'form':form
    }
    return render(request,'karyawan/edit.html',context)

#========================================================================================================================
def show(request,id):
    data_karyawan =get_object_or_404(Karyawan,pk=id) 
    context = {
        'karyawan':data_karyawan,
    }
    return render(request,'karyawan/show.html',context)

#========================================================================================================================
def destroy(request,id):
    if request.method == 'POST':
        data_karyawan_dihapus = Karyawan.objects.get(id=id)
        try:
            data_karyawan_dihapus.delete()
            messages.success(request, 'Data Berhasil Dihapus')
            return redirect('karyawan:index')
        except ProtectedError:
            messages.error(request, 'Data Gagal Dihapus')
            return redirect('karyawan:destroy',id=id)
    
    data_karyawan =get_object_or_404(Karyawan,pk=id) 
    context = {
        'karyawan':data_karyawan,
    }
    return render(request,'karyawan/delete.html',context)