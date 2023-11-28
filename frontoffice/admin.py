from django.contrib import admin
from .models import registrasi

class registrasiAdmin(admin.ModelAdmin):
    list_filter=("no_rawat","no_registrasi","tgl_registrasi","pasien","dokter","poliklinik")
    list_display = ("no_rawat","no_registrasi","tgl_registrasi","pasien","dokter","poliklinik")
    readonly_fields = ("no_rawat","no_registrasi")

admin.site.register(registrasi,registrasiAdmin)