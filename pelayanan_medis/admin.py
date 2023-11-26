from django.contrib import admin
from .models import perawatan_rawat_jalan_pasien

#===========================================================================================================================
class perawatanRawatJalanPasienAdmin(admin.ModelAdmin):
    list_filter=("no_rawat","total_biaya")
    list_display = ("no_rawat","tgl_perawatan","perawatan_rawat_jalan","kategori","dokter","petugas","jumlah_total_biaya")
    readonly_fields = ("kategori","nama_perawatan","biaya_material","biaya_bhp","biaya_dokter","biaya_perawat","biaya_kso","biaya_manajemen","biaya_rawat","total_biaya")
    
    def jumlah_total_biaya(self, obj):
        rupiah = "{:0,.0f}".format(float(obj.total_biaya))
        return "Rp. {}".format(rupiah)
    
admin.site.register(perawatan_rawat_jalan_pasien,perawatanRawatJalanPasienAdmin)
# Register your models here.
