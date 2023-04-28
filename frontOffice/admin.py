from django.contrib import admin
from .models import registrasiPasien

class registrasiPasienAdmin(admin.ModelAdmin):
    list_filter=("no_rawat","no_registrasi","tgl_registrasi","jam_registrasi","pasien","dokter","poliklinik")
    list_display = ("no_rawat","no_registrasi","tgl_registrasi","jam_registrasi","pasien","dokter","poliklinik")
    readonly_fields = ("no_rawat","no_registrasi")

admin.site.register(registrasiPasien,registrasiPasienAdmin)