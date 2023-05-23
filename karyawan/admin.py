from django.contrib import admin
from .models import StatusKaryawan,Karyawan,JabatanKaryawan,GolonganKaryawan,KategoriBerkasKaryawan,BerkasKaryawan
# Register your models here.

#===========================================================================================================================
class StatusKaryawanAdmin(admin.ModelAdmin):
    fields = ['name']

admin.site.register(StatusKaryawan, StatusKaryawanAdmin)

#===========================================================================================================================
class JabatanKaryawanAdmin(admin.ModelAdmin):
    fields = ['nama','keterangan']
    list_display = ('nama','keterangan')

admin.site.register(JabatanKaryawan, JabatanKaryawanAdmin)

#===========================================================================================================================
class GolonganKaryawanAdmin(admin.ModelAdmin):
    fields = ['nama','keterangan']
    list_display = ('nama','keterangan')

admin.site.register(GolonganKaryawan, GolonganKaryawanAdmin)

#===========================================================================================================================
class KategoriBerkasKaryawanAdmin(admin.ModelAdmin):
    fields = ['nama']

admin.site.register(KategoriBerkasKaryawan, KategoriBerkasKaryawanAdmin)

#===========================================================================================================================
class BerkasKaryawanAdmin(admin.ModelAdmin):
    fields = ['karyawan','nama_berkas','kategori','berkas','verifikator','keterangan_verifikator']
    list_display = ('karyawan','nama_berkas','kategori','berkas','verifikator','keterangan_verifikator')

admin.site.register(BerkasKaryawan, BerkasKaryawanAdmin)

#===========================================================================================================================
class KaryawanAdmin(admin.ModelAdmin):
    list_display = ("nama", "nama_lengkap", "user","status_karyawan","agama","jenis_kelamin","golongan_darah","status_nikah","golongan_karyawan","jabatan_karyawan","unit")
    list_filter = ["nama_lengkap","status_karyawan","golongan_karyawan","jabatan_karyawan"]
admin.site.register(Karyawan, KaryawanAdmin)
