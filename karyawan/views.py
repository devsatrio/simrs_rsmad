from django.shortcuts import render
from .tables import KaryawanTable
from .models import Karyawan
from .filters import KaryawanFilter
from django.shortcuts import get_object_or_404
from django_tables2 import RequestConfig

def index(request):
    f = KaryawanFilter(request.GET, queryset=Karyawan.objects.all())
    table_karyawan = KaryawanTable(f.qs)
    context = {
        'tabel_karyawan':table_karyawan,
        'filter':f,
    }
    return render(request,'karyawan/index.html',context)

def show(request,id):
    data_karyawan =get_object_or_404(Karyawan,pk=id) 
    context = {
        'karyawan':data_karyawan,
    }
    return render(request,'karyawan/show.html',context)

def destroy(request,id):
    data_karyawan =get_object_or_404(Karyawan,pk=id) 
    context = {
        'karyawan':data_karyawan,
    }
    return render(request,'karyawan/delete.html',context)