from django.shortcuts import render,redirect
from django.http import JsonResponse
from .tables import KaryawanTable,BerkasSayaTable,BerkasKaryawanTable,KarirKaryawanTable,RiwayatPendidikanKaryawanTable,PelatihanKaryawanTable,KarirSayaTable,RiwayatPendidikanSayaTable,PelatihanSayaTable,AbsensiKaryawanTable
from .models import Karyawan,BerkasKaryawan,KarirKaryawan,RiwayatPendidikanKaryawan,PelatihanKaryawan,AbsensiKaryawan
from .filters import KaryawanFilter,BerkasSayaFilter,BerkasKaryawanFilter,KarirKaryawanFilter,RiwayatPendidikanKaryawanFilter,PelatihanKaryawanFilter,KarirSayaFilter,RiwayatPendidikanSayaFilter,PelatihanSayaFilter,AbsensiKaryawanFilter
from .forms import KaryawanForm,BerkasSayaForm,BerkasKaryawanForm,KarirKaryawanForm,RiwayatPendidikanKaryawanForm,PelatihanKaryawanForm,KarirSayaForm,RiwayatPendidikanSayaForm,PelatihanSayaForm,DataKaryawanSayaForm
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.db.models import ProtectedError
from django_tables2 import RequestConfig
from django.contrib.auth.decorators import login_required,permission_required

#========================================================================================================================
@login_required
@permission_required('karyawan.view_absensikaryawan')
def showabsensikaryawan(request,id):
    data =get_object_or_404(AbsensiKaryawan,pk=id) 
    context = {
        'title':'Absensi Karyawan',
        'data':data,
    }
    return render(request,'absensi_karyawan/show.html',context)

#========================================================================================================================
@login_required
@permission_required('karyawan.view_absensikaryawan')
def indexabsensikaryawan(request):
    f = AbsensiKaryawanFilter(request.GET, queryset=AbsensiKaryawan.objects.all().order_by('-pk'))
    table_absensi_karyawan = AbsensiKaryawanTable(f.qs)
    table_absensi_karyawan.paginate(page=request.GET.get("page", 1), per_page=50)
    context = {
        'tabelnya':table_absensi_karyawan,
        'title':'Absensi Karyawan',
        'filter':f,
    }
    return render(request,'absensi_karyawan/index.html',context)

#========================================================================================================================
@login_required
def datakaryawansaya(request):
    user = request.user
    cek_relasi = Karyawan.objects.filter(user=user).count()
    if(cek_relasi<=0):
            messages.error(request, 'User tidak memiliki relasi dengan karyawan')
            return redirect('dashboard')
    else:
        obj = get_object_or_404(Karyawan, user = user)
        if request.method == 'POST':
            form = DataKaryawanSayaForm(request.POST or None,request.FILES, instance = obj)
            if form.is_valid():
                form.save()
                messages.success(request, 'Data Berhasil Diedit')
                return redirect('karyawan:data-karyawan-saya')
        else:
            form = DataKaryawanSayaForm(request.POST or None,instance = obj)
        
        context={
            'form':form,
            'title':'Data Karyawan Saya',
            'status_form':'Edit Data',
        }
    return render(request,'data_karyawan_saya/form.html',context)

#========================================================================================================================
@login_required
def cv_karyawan(request,id):
    data_karyawan = get_object_or_404(Karyawan, id = id)
    data_riwayat_pendidikan = RiwayatPendidikanKaryawan.objects.filter(karyawan=Karyawan.objects.get(id=id))
    data_pelatihan = PelatihanKaryawan.objects.filter(karyawan=Karyawan.objects.get(id=id))
    data_karir = KarirKaryawan.objects.filter(karyawan=Karyawan.objects.get(id=id))
    data_berkas = BerkasKaryawan.objects.filter(karyawan=Karyawan.objects.get(id=id)).filter(status_berkas='Berkas Diterima')
    context = {
        'data':data_karyawan,
        'data_riwayat_pendidikan':data_riwayat_pendidikan,
        'data_pelatihan':data_pelatihan,
        'data_karir':data_karir,
        'data_berkas':data_berkas,
    }
    return render(request,'karyawan/cv.html',context)

#========================================================================================================================
@login_required
@permission_required('karyawan.cv_saya')
def cv_saya(request):
    user = request.user
    cek_relasi = Karyawan.objects.filter(user=user).count()
    if(cek_relasi<=0):
            messages.error(request, 'User tidak memiliki relasi dengan karyawan')
            return redirect('dashboard')
    else:
        data_karyawan = get_object_or_404(Karyawan, user = user)
        data_riwayat_pendidikan = RiwayatPendidikanKaryawan.objects.filter(karyawan=Karyawan.objects.get(user=user))
        data_pelatihan = PelatihanKaryawan.objects.filter(karyawan=Karyawan.objects.get(user=user))
        data_karir = KarirKaryawan.objects.filter(karyawan=Karyawan.objects.get(user=user))
        data_berkas = BerkasKaryawan.objects.filter(karyawan=Karyawan.objects.get(user=user)).filter(status_berkas='Berkas Diterima')
        context = {
            'data':data_karyawan,
            'data_riwayat_pendidikan':data_riwayat_pendidikan,
            'data_pelatihan':data_pelatihan,
            'data_karir':data_karir,
            'data_berkas':data_berkas,
        }
    return render(request,'cv_saya/index.html',context)

#========================================================================================================================
@login_required
@permission_required('karyawan.pelatihan_saya')
def destroypelatihansaya(request,id):
    user = request.user
    cek_relasi = Karyawan.objects.filter(user=user).count()
    if(cek_relasi<=0):
            messages.error(request, 'User tidak memiliki relasi dengan karyawan')
            return redirect('dashboard')
    else:
        if request.method == 'POST':
            data_dihapus = PelatihanKaryawan.objects.get(id=id)
            try:
                data_dihapus.delete()
                messages.success(request, 'Data Berhasil Dihapus')
                return redirect('karyawan:pelatihan-saya-index')
            except ProtectedError:
                messages.error(request, 'Data Gagal Dihapus')
                return redirect('karyawan:pelatihan-saya-destroy',id=id)
        
        data =get_object_or_404(PelatihanKaryawan,pk=id) 
        context = {
            'data':data,
        }
    return render(request,'pelatihan_saya/delete.html',context)

#========================================================================================================================
@login_required
@permission_required('karyawan.pelatihan_saya')
def editpelatihansaya(request,id):
    user = request.user
    cek_relasi = Karyawan.objects.filter(user=user).count()
    if(cek_relasi<=0):
            messages.error(request, 'User tidak memiliki relasi dengan karyawan')
            return redirect('dashboard')
    else:
        obj = get_object_or_404(PelatihanKaryawan, id = id)
        form = PelatihanSayaForm(request.user,request.POST or None, instance = obj)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data Berhasil Diedit')
            return redirect('karyawan:pelatihan-karyawan-index')
        
        context={
            'form':form,
            'title':'Pelatihan Saya',
            'status_form':'Edit Data',
        }
    return render(request,'pelatihan_saya/form.html',context)

#========================================================================================================================
@login_required
@permission_required('karyawan.pelatihan_saya')
def showpelatihansaya(request,id):
    data =get_object_or_404(PelatihanKaryawan,pk=id) 
    context = {
        'title':'Pelatihan Saya',
        'data':data,
    }
    return render(request,'pelatihan_saya/show.html',context)


#========================================================================================================================
@login_required
@permission_required('karyawan.pelatihan_saya')
def createpelatihansaya(request):
    user = request.user
    cek_relasi = Karyawan.objects.filter(user=user).count()
    if(cek_relasi<=0):
            messages.error(request, 'User tidak memiliki relasi dengan karyawan')
            return redirect('dashboard')
    else:
        form = PelatihanSayaForm(request.user,request.POST or None)
        if form.is_valid():
            obj = form.save(commit=False) # Return an object without saving to the DB
            obj.karyawan = Karyawan.objects.get(user=user) # Add an author field which will contain current user's id
            obj.save()

            messages.success(request, 'Data Berhasil Disimpan')
            return redirect('karyawan:pelatihan-saya-index')
        
        context={
            'form':form,
            'title':'Pelatihan Karyawan',
            'status_form':'Edit Data',
        }
    return render(request,'pelatihan_saya/form.html',context)

#========================================================================================================================
@login_required
@permission_required('karyawan.pelatihan_saya')
def indexpelatihansaya(request):
    user = request.user
    cek_relasi = Karyawan.objects.filter(user=user).count()
    if(cek_relasi<=0):
            messages.error(request, 'User tidak memiliki relasi dengan karyawan')
            return redirect('dashboard')
    else:
        f = PelatihanSayaFilter(request.GET, queryset=PelatihanKaryawan.objects.all().filter(karyawan=Karyawan.objects.get(user=user)).order_by('-pk'))
        tabelnya = PelatihanSayaTable(f.qs)
        tabelnya.paginate(page=request.GET.get("page", 1), per_page=50)
        context = {
            'title':'Pelatihan Saya',
            'tabelnya':tabelnya,
            'filter':f,
        }
    return render(request,'pelatihan_saya/index.html',context)

#========================================================================================================================
@login_required
@permission_required('karyawan.riwayat_pendidikan_saya')
def destroyriwayatpendidikansaya(request,id):
    if request.method == 'POST':
        data_dihapus = RiwayatPendidikanKaryawan.objects.get(id=id)
        try:
            data_dihapus.delete()
            messages.success(request, 'Data Berhasil Dihapus')
            return redirect('karyawan:riwayat-pendidikan-saya-index')
        except ProtectedError:
            messages.error(request, 'Data Gagal Dihapus')
            return redirect('karyawan:riwayat-pendidikan-saya-destroy',id=id)
    
    data =get_object_or_404(RiwayatPendidikanKaryawan,pk=id) 
    context = {
        'data':data,
    }
    return render(request,'riwayat_pendidikan_saya/delete.html',context)

#========================================================================================================================
@login_required
@permission_required('karyawan.riwayat_pendidikan_saya')
def editriwayatpendidikansaya(request,id):
    user = request.user
    obj = get_object_or_404(RiwayatPendidikanKaryawan, id = id)
    cek_relasi = Karyawan.objects.filter(user=user).count()
    if(cek_relasi<=0):
            messages.error(request, 'User tidak memiliki relasi dengan karyawan')
            return redirect('dashboard')
    else:
        if request.method == 'POST':
            form = RiwayatPendidikanSayaForm(request.user, request.POST,instance=obj)
            if form.is_valid():
                obj = form.save(commit=False) # Return an object without saving to the DB
                obj.karyawan = Karyawan.objects.get(user=user) # Add an author field which will contain current user's id
                obj.save()

                # form.save()
                messages.success(request, 'Data Berhasil Disimpan')
                return redirect('karyawan:riwayat-pendidikan-saya-index')
        else:
            form = RiwayatPendidikanSayaForm(request.user,instance=obj)
        context={
            'title':'Riwayat Pendidikan Saya',
            'status_form':'Edit Data',
            'form':form
        }
    return render(request,'riwayat_pendidikan_saya/form.html',context)

#========================================================================================================================
@login_required
@permission_required('karyawan.riwayat_pendidikan_saya')
def showriwayatpendidikansaya(request,id):
    data =get_object_or_404(RiwayatPendidikanKaryawan,pk=id) 
    context = {
        'title':'Riwayat Pendidikan Saya',
        'data':data,
    }
    return render(request,'riwayat_pendidikan_saya/show.html',context)

#========================================================================================================================
@login_required
@permission_required('karyawan.riwayat_pendidikan_saya')
def createriwayatpendidikansaya(request):
    user = request.user
    cek_relasi = Karyawan.objects.filter(user=user).count()
    if(cek_relasi<=0):
            messages.error(request, 'User tidak memiliki relasi dengan karyawan')
            return redirect('dashboard')
    else:
        if request.method == 'POST':
            form = RiwayatPendidikanSayaForm(request.user, request.POST)
            if form.is_valid():
                obj = form.save(commit=False) # Return an object without saving to the DB
                obj.karyawan = Karyawan.objects.get(user=user) # Add an author field which will contain current user's id
                obj.save()

                # form.save()
                messages.success(request, 'Data Berhasil Disimpan')
                return redirect('karyawan:riwayat-pendidikan-saya-index')
        else:
            form = RiwayatPendidikanSayaForm(request.user)
        context={
            'title':'Riwayat Pendidikan Saya',
            'status_form':'Add Data',
            'form':form
        }
    return render(request,'riwayat_pendidikan_saya/form.html',context)

#========================================================================================================================
@login_required
@permission_required('karyawan.riwayat_pendidikan_saya')
def indexriwayatpendidikansaya(request):
    user = request.user
    cek_relasi = Karyawan.objects.filter(user=user).count()
    if(cek_relasi<=0):
            messages.error(request, 'User tidak memiliki relasi dengan karyawan')
            return redirect('dashboard')
    else:
        f = RiwayatPendidikanSayaFilter(request.GET, queryset=RiwayatPendidikanKaryawan.objects.filter(karyawan=Karyawan.objects.get(user=user)).order_by('-pk'))
        tabelnya = RiwayatPendidikanSayaTable(f.qs)
        tabelnya.paginate(page=request.GET.get("page", 1), per_page=50)
        context = {
            'title':'Riwayat Pendidikan Saya',
            'tabelnya':tabelnya,
            'filter':f,
        }
    return render(request,'riwayat_pendidikan_saya/index.html',context)

#========================================================================================================================
@login_required
@permission_required('karyawan.karir_saya')
def destroykarirsaya(request,id):
    if request.method == 'POST':
        data_dihapus = KarirKaryawan.objects.get(id=id)
        try:
            data_dihapus.delete()
            messages.success(request, 'Data Berhasil Dihapus')
            return redirect('karyawan:karir-saya-index')
        except ProtectedError:
            messages.error(request, 'Data Gagal Dihapus')
            return redirect('karyawan:karir-saya-destroy',id=id)
    
    data =get_object_or_404(KarirKaryawan,pk=id) 
    context = {
        'data':data,
    }
    return render(request,'karir_saya/delete.html',context)

#========================================================================================================================
@login_required
@permission_required('karyawan.karir_saya')
def editkarirsaya(request,id):
    obj = get_object_or_404(KarirKaryawan, id = id)
    user = request.user
    cek_relasi = Karyawan.objects.filter(user=user).count()
    if(cek_relasi<=0):
            messages.error(request, 'User tidak memiliki relasi dengan karyawan')
            return redirect('dashboard')
    else:
        if request.method == 'POST':
            form = KarirSayaForm(request.user, request.POST, instance = obj)
            if form.is_valid():
                obj = form.save(commit=False) # Return an object without saving to the DB
                obj.karyawan = Karyawan.objects.get(user=user) # Add an author field which will contain current user's id
                obj.save()

                # form.save()
                messages.success(request, 'Data Berhasil Disimpan')
                return redirect('karyawan:karir-saya-index')
        else:
            form = KarirSayaForm(request.user, instance = obj)
        context={
            'title':'Karir Saya',
            'status_form':'Edit Data',
            'form':form
        }
        return render(request,'karir_saya/form.html',context)

#========================================================================================================================
@login_required
@permission_required('karyawan.karir_saya')
def showkarirsaya(request,id):
    data =get_object_or_404(KarirKaryawan,pk=id) 
    context = {
        'title':'Karir Saya',
        'data':data,
    }
    return render(request,'karir_saya/show.html',context)

#========================================================================================================================
@login_required
@permission_required('karyawan.karir_saya')
def createkarirsaya(request):
    user = request.user
    cek_relasi = Karyawan.objects.filter(user=user).count()
    if(cek_relasi<=0):
            messages.error(request, 'User tidak memiliki relasi dengan karyawan')
            return redirect('dashboard')
    else:
        if request.method == 'POST':
            form = KarirSayaForm(request.user, request.POST)
            if form.is_valid():
                obj = form.save(commit=False) # Return an object without saving to the DB
                obj.karyawan = Karyawan.objects.get(user=user) # Add an author field which will contain current user's id
                obj.save()

                # form.save()
                messages.success(request, 'Data Berhasil Disimpan')
                return redirect('karyawan:karir-saya-index')
        else:
            form = KarirSayaForm(request.user)
        context={
            'title':'Karir Saya',
            'status_form':'Add Data',
            'form':form
        }
        return render(request,'karir_saya/form.html',context)
    
#========================================================================================================================
@login_required
@permission_required('karyawan.karir_saya')
def indexkarirsaya(request):
    user = request.user
    cek_relasi = Karyawan.objects.filter(user=user).count()
    if(cek_relasi<=0):
            messages.error(request, 'User tidak memiliki relasi dengan karyawan')
            return redirect('dashboard')
    else:
        f = KarirSayaFilter(request.GET, queryset=KarirKaryawan.objects.filter(karyawan=Karyawan.objects.get(user=user)).order_by('-pk'))
        tabelnya = KarirSayaTable(f.qs)
        tabelnya.paginate(page=request.GET.get("page", 1), per_page=50)
        context = {
            'title':'Karir Saya',
            'tabelnya':tabelnya,
            'filter':f,
        }
    return render(request,'karir_saya/index.html',context)

#========================================================================================================================
@login_required
@permission_required('karyawan.delete_pelatihankaryawan')
def destroypelatihankaryawan(request,id):
    if request.method == 'POST':
        data_dihapus = PelatihanKaryawan.objects.get(id=id)
        try:
            data_dihapus.delete()
            messages.success(request, 'Data Berhasil Dihapus')
            return redirect('karyawan:pelatihan-karyawan-index')
        except ProtectedError:
            messages.error(request, 'Data Gagal Dihapus')
            return redirect('karyawan:pelatihan-karyawan-destroy',id=id)
    
    data =get_object_or_404(PelatihanKaryawan,pk=id) 
    context = {
        'data':data,
    }
    return render(request,'pelatihan_karyawan/delete.html',context)

#========================================================================================================================
@login_required
@permission_required('karyawan.change_pelatihankaryawan')
def editpelatihankaryawan(request,id):
    obj = get_object_or_404(PelatihanKaryawan, id = id)
    form = PelatihanKaryawanForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        messages.success(request, 'Data Berhasil Diedit')
        return redirect('karyawan:pelatihan-karyawan-index')
    
    context={
        'form':form,
        'title':'Pelatihan Karyawan',
        'status_form':'Edit Data',
    }
    return render(request,'pelatihan_karyawan/form.html',context)

#========================================================================================================================
@login_required
@permission_required('karyawan.view_pelatihankaryawan')
def showpelatihankaryawan(request,id):
    data =get_object_or_404(PelatihanKaryawan,pk=id) 
    context = {
        'title':'Pelatihan Karyawan',
        'data':data,
    }
    return render(request,'pelatihan_karyawan/show.html',context)

#========================================================================================================================
@login_required
@permission_required('karyawan.add_pelatihankaryawan')
def createpelatihankaryawan(request):
    form = PelatihanKaryawanForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Data Berhasil Disimpan')
        return redirect('karyawan:pelatihan-karyawan-index')
    
    context={
        'form':form,
        'title':'Pelatihan Karyawan',
        'status_form':'Add Data',
    }
    return render(request,'pelatihan_karyawan/form.html',context)

#========================================================================================================================
@login_required
@permission_required('karyawan.view_pelatihankaryawan')
def indexpelatihankaryawan(request):
    f = PelatihanKaryawanFilter(request.GET, queryset=PelatihanKaryawan.objects.all().order_by('-pk'))
    tabelnya = PelatihanKaryawanTable(f.qs)
    tabelnya.paginate(page=request.GET.get("page", 1), per_page=50)
    context = {
        'title':'Pelatihan Karyawan',
        'tabelnya':tabelnya,
        'filter':f,
    }
    return render(request,'pelatihan_karyawan/index.html',context)

#========================================================================================================================
@login_required
@permission_required('karyawan.delete_riwayatpendidikankaryawan')
def destroyriwayatpendidikankaryawan(request,id):
    if request.method == 'POST':
        data_dihapus = RiwayatPendidikanKaryawan.objects.get(id=id)
        try:
            data_dihapus.delete()
            messages.success(request, 'Data Berhasil Dihapus')
            return redirect('karyawan:riwayat-pendidikan-karyawan-index')
        except ProtectedError:
            messages.error(request, 'Data Gagal Dihapus')
            return redirect('karyawan:riwayat-pendidikan-karyawan-destroy',id=id)
    
    data =get_object_or_404(RiwayatPendidikanKaryawan,pk=id) 
    context = {
        'data':data,
    }
    return render(request,'riwayat_pendidikan_karyawan/delete.html',context)

    
#========================================================================================================================
@login_required
@permission_required('karyawan.change_riwayatpendidikankaryawan')
def editriwayatpendidikankaryawan(request,id):
    obj = get_object_or_404(RiwayatPendidikanKaryawan, id = id)
    form = RiwayatPendidikanKaryawanForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        messages.success(request, 'Data Berhasil Diedit')
        return redirect('karyawan:riwayat-pendidikan-karyawan-index')
    
    context={
        'form':form,
        'title':'Riwayat Pendidikan Karyawan',
        'status_form':'Edit Data',
    }
    return render(request,'riwayat_pendidikan_karyawan/form.html',context)

#========================================================================================================================
@login_required
@permission_required('karyawan.view_riwayatpendidikankaryawan')
def showriwayatpendidikankaryawan(request,id):
    data =get_object_or_404(RiwayatPendidikanKaryawan,pk=id) 
    context = {
        'title':'Riwayat Pendidikan Karyawan',
        'data':data,
    }
    return render(request,'riwayat_pendidikan_karyawan/show.html',context)

#========================================================================================================================
@login_required
@permission_required('karyawan.add_riwayatpendidikankaryawan')
def createriwayatpendidikankaryawan(request):
    form = RiwayatPendidikanKaryawanForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Data Berhasil Disimpan')
        return redirect('karyawan:riwayat-pendidikan-karyawan-index')
    
    context={
        'form':form,
        'title':'Riwayat Pendidikan Karyawan',
        'status_form':'Add Data',
    }
    return render(request,'riwayat_pendidikan_karyawan/form.html',context)

#========================================================================================================================
@login_required
@permission_required('karyawan.view_riwayatpendidikankaryawan')
def indexriwayatpendidikankaryawan(request):
    f = RiwayatPendidikanKaryawanFilter(request.GET, queryset=RiwayatPendidikanKaryawan.objects.all().order_by('-pk'))
    tabelnya = RiwayatPendidikanKaryawanTable(f.qs)
    tabelnya.paginate(page=request.GET.get("page", 1), per_page=50)
    context = {
        'title':'Riwayat Pendidikan Karyawan',
        'tabelnya':tabelnya,
        'filter':f,
    }
    return render(request,'riwayat_pendidikan_karyawan/index.html',context)

#========================================================================================================================
@login_required
@permission_required('karyawan.view_karirkaryawan')
def indexkarirkaryawan(request):
    f = KarirKaryawanFilter(request.GET, queryset=KarirKaryawan.objects.all().order_by('-pk'))
    tabelnya = KarirKaryawanTable(f.qs)
    tabelnya.paginate(page=request.GET.get("page", 1), per_page=50)
    context = {
        'title':'Karir Karyawan',
        'tabelnya':tabelnya,
        'filter':f,
    }
    return render(request,'karir_karyawan/index.html',context)

#========================================================================================================================
@login_required
@permission_required('karyawan.add_karirkaryawan')
def createkarirkaryawan(request):
    form = KarirKaryawanForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Data Berhasil Disimpan')
        return redirect('karyawan:karir-karyawan-index')
    
    context={
        'form':form,
        'title':'Karir Karyawan',
        'status_form':'Add Data',
    }
    return render(request,'karir_karyawan/form.html',context)

#========================================================================================================================
@login_required
@permission_required('karyawan.view_karirkaryawan')
def showkarirkaryawan(request,id):
    data =get_object_or_404(KarirKaryawan,pk=id) 
    context = {
        'title':'Karir Karyawan',
        'data':data,
    }
    return render(request,'karir_karyawan/show.html',context)

#========================================================================================================================
@login_required
@permission_required('karyawan.change_karirkaryawan')
def editkarirkaryawan(request,id):
    obj = get_object_or_404(KarirKaryawan, id = id)
    form = KarirKaryawanForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        messages.success(request, 'Data Berhasil Diedit')
        return redirect('karyawan:karir-karyawan-index')
    
    context={
        'form':form,
        'title':'Karir Karyawan',
        'status_form':'Edit Data',
    }
    return render(request,'karir_karyawan/form.html',context)

#========================================================================================================================
@login_required
@permission_required('karyawan.delete_karirkaryawan')
def destroykarirkaryawan(request,id):
    if request.method == 'POST':
        data_karyawan_dihapus = KarirKaryawan.objects.get(id=id)
        try:
            data_karyawan_dihapus.delete()
            messages.success(request, 'Data Berhasil Dihapus')
            return redirect('karyawan:karir-karyawan-index')
        except ProtectedError:
            messages.error(request, 'Data Gagal Dihapus')
            return redirect('karyawan:karir-karyawan-destroy',id=id)
    
    data =get_object_or_404(KarirKaryawan,pk=id) 
    context = {
        'data':data,
    }
    return render(request,'karir_karyawan/delete.html',context)

#========================================================================================================================
@login_required
def berkas_list(request,karyawan_id):
    berkas_data = BerkasKaryawan.objects.filter(karyawan=karyawan_id).filter(status_berkas='Berkas Diterima')
    return JsonResponse({'data': [{'id': k.id, 'name': k.nama_berkas} for k in berkas_data]})

#========================================================================================================================
@login_required
@permission_required('karyawan.view_karyawan')
def index(request):
    f = KaryawanFilter(request.GET, queryset=Karyawan.objects.all().order_by('-pk'))
    table_karyawan = KaryawanTable(f.qs)
    table_karyawan.paginate(page=request.GET.get("page", 1), per_page=50)
    context = {
        'tabel_karyawan':table_karyawan,
        'filter':f,
    }
    print(f)
    return render(request,'karyawan/index.html',context)

#========================================================================================================================
@login_required
@permission_required('karyawan.add_karyawan')
def create(request):
    if request.method == 'POST':
        form = KaryawanForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data Berhasil Disimpan')
            return redirect('karyawan:index')
    else:
        form = KaryawanForm()
    context={
        'form':form
    }
    return render(request,'karyawan/create.html',context)

#========================================================================================================================
@login_required
@permission_required('karyawan.change_karyawan')
def edit(request,id):
    obj = get_object_or_404(Karyawan, id = id)
    if request.method == 'POST':
        form = KaryawanForm(request.POST, request.FILES, instance = obj)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data Berhasil Diedit')
            return redirect('karyawan:index')
    else:
        form = KaryawanForm(instance = obj)
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
    cek_relasi = Karyawan.objects.filter(user=user).count()
    if(cek_relasi<=0):
            messages.error(request, 'User tidak memiliki relasi dengan karyawan')
            return redirect('dashboard')
    else:
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
            return redirect('dashboard')
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
            return redirect('dashboard')
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