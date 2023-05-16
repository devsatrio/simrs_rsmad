from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

def index(request):
    return render(request,'index.html')

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

@login_required
def dashboard(request):
    return render(request,'dashboard.html')