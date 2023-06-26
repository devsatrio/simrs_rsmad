"""
URL configuration for simrs_rsmad project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, reverse_lazy
from django.views.generic.base import RedirectView
from django.conf import settings #add this
from django.conf.urls.static import static #add this
from crudbuilder import urls
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('admin/', admin.site.urls),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('captcha/', include('captcha.urls')),
    path('dashboard',views.dashboard,name='dashboard'),
    path('dashboard/profile',views.profile,name='profile'),
    path('dashboard/edit-profile',views.editprofile,name='editprofile'),
    path('dashboard/edit-profile-pass',views.editprofilepass,name='editprofilepass'),
    path('pasien/', include('pasien.urls')),
    path('crud/',  include('crudbuilder.urls')),
    path('karyawan/',include('karyawan.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
