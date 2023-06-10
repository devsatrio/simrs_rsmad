from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .forms import UserUpdateForm,UserUpdatePassForm

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
        username = request.POST['username']
        password = request.POST['password']

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
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:    
        return render(request,'login.html')

def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
        return redirect('index')
    else:
        return redirect('index')

#========================================================================================================================
@login_required
def dashboard(request):
    return render(request,'dashboard.html')