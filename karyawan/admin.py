from django.contrib import admin
from .models import StatusKaryawan,Karyawan
# Register your models here.

class StatusKaryawanAdmin(admin.ModelAdmin):
    fields = ['name']

admin.site.register(StatusKaryawan, StatusKaryawanAdmin)

class KaryawanAdmin(admin.ModelAdmin):
    list_display = ("nama", "nama_lengkap", "user","status_karyawan","agama","jenis_kelamin","golongan_darah","status_nikah")
    list_filter = ["status_karyawan"]
admin.site.register(Karyawan, KaryawanAdmin)
