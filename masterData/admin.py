from django.contrib import admin
from .models import Agama,GolonganDarah,JenisKelamin,StatusNikah,JenisPekerjaan, StrataPendidikan, Asuransi, Poliklinik,Bangsal

# Register your models here.

admin.site.register(Agama)
admin.site.register(GolonganDarah)
admin.site.register(JenisKelamin)
admin.site.register(StatusNikah)
admin.site.register(JenisPekerjaan)
admin.site.register(StrataPendidikan)
admin.site.register(Asuransi)

class PoliklinikAdmin(admin.ModelAdmin):
    list_display = ["kode","name"]

admin.site.register(Poliklinik,PoliklinikAdmin)

class BangsalAdmin(admin.ModelAdmin):
    list_display = ["kode","name","status"]

admin.site.register(Bangsal,BangsalAdmin)