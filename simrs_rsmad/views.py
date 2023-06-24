from django.shortcuts import render,redirect
from django.contrib import messages
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.admin.models import ADDITION, LogEntry
from karyawan.models import Karyawan,BerkasKaryawan
from .forms import UserUpdateForm,UserUpdatePassForm,CaptchaLoginForm

#========================================================================================================================
def index(request):
    return render(request,'index.html')

#========================================================================================================================
@login_required
def profile(request):
    context={
        'data':request.user,
        'title':'Profile',
    }
    return render(request,'profile.html',context)

#========================================================================================================================
@login_required
def editprofilepass(request):
    user = request.user
    if request.method == 'POST':
        form = UserUpdatePassForm(user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your password has been changed")
            return redirect('login')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

    form = UserUpdatePassForm(user)
    
    context={
        'form':form,
        'title':'Profile',
        'status_form':'Edit Password',
    }
    return render(request,'edit_profile.html',context)

#========================================================================================================================
@login_required
def editprofile(request):
    form = UserUpdateForm(request.POST or None,instance=request.user)
    if form.is_valid():
        form.save()
        messages.success(request, 'Data Berhasil Disimpan')
        return redirect('dashboard')
    
    context={
        'form':form,
        'title':'Profile',
        'status_form':'Edit Data',
    }
    return render(request,'edit_profile.html',context)

#========================================================================================================================
def login(request):
    if request.method == 'POST':
        captcha_form = CaptchaLoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        if captcha_form.is_valid():
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    auth_login(request, user)
                    #messages.success(request, 'Berhasil Membuat akun')
                    return redirect('dashboard')
                else:
                    messages.error(request, 'Akun tidak aktif')
                    return redirect('login')
            else:
                messages.error(request, 'Username / Password salah')
                return redirect('login')
        else:
            messages.error(request, 'Captcha Salah')
            return redirect('login')
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        captcha_form = CaptchaLoginForm()
        context = {
            'captcha_form':captcha_form
        }
        return render(request,'login.html',context)

#========================================================================================================================
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
        return redirect('index')
    else:
        return redirect('index')

#========================================================================================================================
@login_required
def dashboard(request):
    user = request.user
    cek_relasi = Karyawan.objects.filter(user=user).count()
    jumlah_berkas_diajukan=BerkasKaryawan.objects.filter(status_berkas='Berkas Diajukan').count()
    jumlah_berkas_ditolak=BerkasKaryawan.objects.filter(status_berkas='Berkas Ditolak').count()
    jumlah_berkas_diterima=BerkasKaryawan.objects.filter(status_berkas='Berkas Diterima').count()
    jumlah_semua_karyawan=Karyawan.objects.all().count()
    jumlah_karyawan_perkategori = Karyawan.objects.all().values('status_karyawan__name').annotate(total=Count('status_karyawan__name')).order_by('total')
    jumlah_karyawan_pergolongan = Karyawan.objects.all().values('golongan_karyawan__nama').annotate(total=Count('golongan_karyawan__nama')).order_by('total')
    berkas_diajukan = BerkasKaryawan.objects.filter(status_berkas='Berkas Diajukan').order_by('-pk')[:10]
    if(cek_relasi>0):
        berkas_saya = BerkasKaryawan.objects.filter(karyawan=Karyawan.objects.get(user=user)).order_by('-pk')[:5]
    else:
        berkas_saya =''

    context={
        'cek_relasi':cek_relasi,
        'user':user,
        'berkas_saya':berkas_saya,
        'jumlah_berkas_diajukan':jumlah_berkas_diajukan,
        'jumlah_berkas_ditolak':jumlah_berkas_ditolak,
        'jumlah_berkas_diterima':jumlah_berkas_diterima,
        'jumlah_semua_karyawan':jumlah_semua_karyawan,
        'jumlah_karyawan_perkategori':jumlah_karyawan_perkategori,
        'jumlah_karyawan_pergolongan':jumlah_karyawan_pergolongan,
        'berkas_diajukan':berkas_diajukan
    }
    return render(request,'dashboard.html',context)