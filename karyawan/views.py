from django.shortcuts import render,redirect
from django.http import JsonResponse
from .tables import KaryawanTable,BerkasSayaTable,BerkasKaryawanTable
from .models import Karyawan,BerkasKaryawan
from .filters import KaryawanFilter,BerkasSayaFilter,BerkasKaryawanFilter
from .forms import KaryawanForm,BerkasSayaForm,BerkasKaryawanForm
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.db.models import ProtectedError
from django_tables2 import RequestConfig
from django.contrib.auth.decorators import login_required,permission_required

#========================================================================================================================
@login_required
def berkas_list(request,karyawan_id):
    berkas_data = BerkasKaryawan.objects.filter(karyawan=karyawan_id).filter(status_berkas='Berkas Diterima')
    return JsonResponse({'data': [{'id': k.id, 'name': k.nama_berkas} for k in berkas_data]})

#========================================================================================================================
@login_required
@permission_required('karyawan.view_karyawan')
def index(request):
    f = KaryawanFilter(request.GET, queryset=Karyawan.objects.all())
    table_karyawan = KaryawanTable(f.qs)
    table_karyawan.paginate(page=request.GET.get("page", 1), per_page=50)
    context = {
        'tabel_karyawan':table_karyawan,
        'filter':f,
    }
    return render(request,'karyawan/index.html',context)

#========================================================================================================================
@login_required
@permission_required('karyawan.add_karyawan')
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
@login_required
@permission_required('karyawan.change_karyawan')
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
@login_required
@permission_required('karyawan.view_karyawan')
def show(request,id):
    data_karyawan =get_object_or_404(Karyawan,pk=id) 
    context = {
        'karyawan':data_karyawan,
    }
    return render(request,'karyawan/show.html',context)

#========================================================================================================================
@login_required
@permission_required('karyawan.delete_karyawan')
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

#========================================================================================================================
@login_required
@permission_required('karyawan.berkas_saya')
def indexberkassaya(request):
    user = request.user
    f = BerkasSayaFilter(request.GET, queryset=BerkasKaryawan.objects.filter(karyawan=Karyawan.objects.get(user=user)).order_by('-pk'))
    tabelnya = BerkasSayaTable(f.qs)
    tabelnya.paginate(page=request.GET.get("page", 1), per_page=50)
    context = {
        'title':'Berkas Saya',
        'tabelnya':tabelnya,
        'filter':f,
    }
    return render(request,'berkas_saya/index.html',context)


#========================================================================================================================
@login_required
@permission_required('karyawan.berkas_saya')
def createberkassaya(request):
    user = request.user
    cek_relasi = Karyawan.objects.filter(user=user).count()
    if(cek_relasi<=0):
            messages.error(request, 'User tidak memiliki relasi dengan karyawan')
            return redirect('karyawan:berkas-saya-index')
    else:
        if request.method == 'POST':
            form = BerkasSayaForm(request.POST, request.FILES)
            if form.is_valid():
                obj = form.save(commit=False) # Return an object without saving to the DB
                obj.karyawan = Karyawan.objects.get(user=user) # Add an author field which will contain current user's id
                obj.status_berkas = 'Berkas Diajukan'
                obj.save()

                # form.save()
                messages.success(request, 'Data Berhasil Disimpan')
                return redirect('karyawan:berkas-saya-index')
        else:
            form = BerkasSayaForm()
        context={
            'title':'Berkas Saya',
            'status_form':'Add Data',
            'form':form
        }
        return render(request,'berkas_saya/form.html',context)

#========================================================================================================================
@login_required
@permission_required('karyawan.berkas_saya')
def editberkassaya(request,id):
    user = request.user
    cek_relasi = Karyawan.objects.filter(user=user).count()
    obj = get_object_or_404(BerkasKaryawan, id = id)
    if(cek_relasi<=0):
            messages.error(request, 'User tidak memiliki relasi dengan karyawan')
            return redirect('karyawan:berkas-saya-index')
    else:
        if request.method == 'POST':
            form = BerkasSayaForm(request.POST, request.FILES,instance = obj)
            if form.is_valid():
                obj = form.save(commit=False) # Return an object without saving to the DB
                obj.karyawan = Karyawan.objects.get(user=user) # Add an author field which will contain current user's id
                obj.status_berkas = 'Berkas Diajukan'
                obj.save()

                # form.save()
                messages.success(request, 'Data Berhasil Disimpan')
                return redirect('karyawan:berkas-saya-index')
        else:
            form = BerkasSayaForm(instance = obj)
        context={
            'form':form,
            'title':'Berkas Saya',
            'status_form':'Edit Data',
        }
        return render(request,'berkas_saya/form.html',context)

#========================================================================================================================
@login_required
@permission_required('karyawan.berkas_saya')
def showberkassaya(request,id):
    data =get_object_or_404(BerkasKaryawan,pk=id) 
    context = {
        'title':'Berkas Saya',
        'data':data,
    }
    return render(request,'berkas_saya/show.html',context)

#========================================================================================================================
@login_required
@permission_required('karyawan.berkas_saya')
def destroyberkassaya(request,id):
    if request.method == 'POST':
        data_dihapus = BerkasKaryawan.objects.get(id=id)
        try:
            data_dihapus.delete()
            messages.success(request, 'Data Berhasil Dihapus')
            return redirect('karyawan:berkas-saya-index')
        except ProtectedError:
            messages.error(request, 'Data Gagal Dihapus')
            return redirect('karyawan:berkas-saya-destroy',id=id)
    
    data =get_object_or_404(BerkasKaryawan,pk=id) 
    context = {
        'data':data,
    }
    return render(request,'berkas_saya/delete.html',context)

#========================================================================================================================
@login_required
@permission_required('karyawan.view_berkaskaryawan')
def indexberkaskaryawan(request):
    f = BerkasKaryawanFilter(request.GET, queryset=BerkasKaryawan.objects.all().order_by('-pk'))
    tabelnya = BerkasKaryawanTable(f.qs)
    tabelnya.paginate(page=request.GET.get("page", 1), per_page=50)
    context = {
        'title':'Berkas Karyawan',
        'tabelnya':tabelnya,
        'filter':f,
    }
    return render(request,'berkas_karyawan/index.html',context)

#========================================================================================================================
@login_required
@permission_required('karyawan.add_berkaskaryawan')
def createberkaskaryawan(request):
    user = request.user
    if request.method == 'POST':
        form = BerkasKaryawanForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False) # Return an object without saving to the DB
            obj.verifikator = user # Add an author field which will contain current user's id
            obj.save()

            # form.save()
            messages.success(request, 'Data Berhasil Disimpan')
            return redirect('karyawan:berkas-karyawan-index')
    else:
        form = BerkasKaryawanForm()
    context={
        'title':'Berkas Karyawan',
        'status_form':'Add Data',
        'form':form
    }
    return render(request,'berkas_karyawan/form.html',context)

#========================================================================================================================
@login_required
@permission_required('karyawan.view_berkaskaryawan')
def showberkaskaryawan(request,id):
    data =get_object_or_404(BerkasKaryawan,pk=id) 
    context = {
        'title':'Berkas Karyawan',
        'data':data,
    }
    return render(request,'berkas_karyawan/show.html',context)

#========================================================================================================================
@login_required
@permission_required('karyawan.change_berkaskaryawan')
def editberkaskaryawan(request,id):
    user = request.user
    form_val = get_object_or_404(BerkasKaryawan, id = id)
    if request.method == 'POST':
        form = BerkasKaryawanForm(request.POST, request.FILES,instance = form_val)
        if form.is_valid():
            obj = form.save(commit=False) # Return an object without saving to the DB
            obj.verifikator = user # Add an author field which will contain current user's id
            obj.save()

            # form.save()
            messages.success(request, 'Data Berhasil Disimpan')
            return redirect('karyawan:berkas-karyawan-index')
    else:
        form = BerkasKaryawanForm(instance = form_val)
    context={
        'form':form,
        'title':'Berkas Karyawan',
        'status_form':'Edit Data',
    }
    return render(request,'berkas_karyawan/form.html',context)

#========================================================================================================================
@login_required
@permission_required('karyawan.delete_berkaskaryawan')
def destroyberkaskaryawan(request,id):
    if request.method == 'POST':
        data_dihapus = BerkasKaryawan.objects.get(id=id)
        try:
            data_dihapus.delete()
            messages.success(request, 'Data Berhasil Dihapus')
            return redirect('karyawan:berkas-karyawan-index')
        except ProtectedError:
            messages.error(request, 'Data Gagal Dihapus')
            return redirect('karyawan:berkas-karyawan-destroy',id=id)
    
    data =get_object_or_404(BerkasKaryawan,pk=id) 
    context = {
        'data':data,
    }
    return render(request,'berkas_saya/delete.html',context)