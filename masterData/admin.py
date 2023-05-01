from django.contrib import admin
from .models import perawatan_rawat_jalan,Agama,GolonganDarah,JenisKelamin,StatusNikah,JenisPekerjaan, StrataPendidikan, Asuransi, Poliklinik,Bangsal,kategori_perawatan

# Register your models here.

admin.site.register(Agama)
admin.site.register(GolonganDarah)
admin.site.register(JenisKelamin)
admin.site.register(StatusNikah)
admin.site.register(JenisPekerjaan)
admin.site.register(StrataPendidikan)
admin.site.register(Asuransi)
admin.site.register(kategori_perawatan)
admin.site.register(perawatan_rawat_jalan)

class PoliklinikAdmin(admin.ModelAdmin):
    list_display = ["kode","name"]

admin.site.register(Poliklinik,PoliklinikAdmin)

class BangsalAdmin(admin.ModelAdmin):
    list_display = ["kode","name","status"]

admin.site.register(Bangsal,BangsalAdmin)