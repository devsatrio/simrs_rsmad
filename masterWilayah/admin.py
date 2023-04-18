from django.contrib import admin
from .models import negara, propinsi, kota, kecamatan, kelurahan
# Register your models here.

class NegaraAdmin(admin.ModelAdmin):
    list_display=("nicename","iso","iso3","phonecode")
admin.site.register(negara,NegaraAdmin)

class PropinsiAdmin(admin.ModelAdmin):
    list_display=("name","negara")
admin.site.register(propinsi,PropinsiAdmin)

class KotaAdmin(admin.ModelAdmin):
    list_display=("name","propinsi")
admin.site.register(kota,KotaAdmin)

class KecamatanAdmin(admin.ModelAdmin):
    list_display=("name","kota")
admin.site.register(kecamatan,KecamatanAdmin)

class kelurahanAdmin(admin.ModelAdmin):
    list_display=("name","kecamatan")
admin.site.register(kelurahan,kelurahanAdmin)
