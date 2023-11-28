from django.contrib import admin
from .models import diagnosa,tindakan

#===========================================================================================================================
class diagnosaAdmin(admin.ModelAdmin):
    list_filter=("no_rawat","diagnosa","status")
    list_display = ("no_rawat","diagnosa","diagnosa_dokter","status","status_periksa","created_by","created_at")

admin.site.register(diagnosa,diagnosaAdmin)

#===========================================================================================================================
class tindakanAdmin(admin.ModelAdmin):
    list_filter=("no_rawat","tindakan","status")
    list_display = ("no_rawat","tindakan","tindakan_dokter","status","status_periksa","created_by","created_at")

admin.site.register(tindakan,tindakanAdmin)
