from django.contrib import admin
from .models import perawatan_rawat_jalan,Agama,GolonganDarah,JenisKelamin,StatusNikah,JenisPekerjaan, StrataPendidikan, Asuransi, Poliklinik,Bangsal,kategori_perawatan,Unit,SatuanBarang,KategoriBarang,Perusahaan,Barang,Ruangan,RuanganUnit
import locale
# Register your models here.

#===========================================================================================================================
admin.site.register(Agama)
admin.site.register(GolonganDarah)
admin.site.register(JenisKelamin)
admin.site.register(StatusNikah)
admin.site.register(JenisPekerjaan)
admin.site.register(StrataPendidikan)
admin.site.register(Asuransi)
admin.site.register(kategori_perawatan)
admin.site.register(perawatan_rawat_jalan)

#===========================================================================================================================
class RuanganUnitAdmin(admin.ModelAdmin):
    list_display = ["unit","ruangan"]

admin.site.register(RuanganUnit,RuanganUnitAdmin)

#===========================================================================================================================
class RuanganAdmin(admin.ModelAdmin):
    list_display = ["kode","name","status"]

admin.site.register(Ruangan,RuanganAdmin)

#===========================================================================================================================
class BarangAdmin(admin.ModelAdmin):
    list_display = ["kode","name","kategori_barang","stok","satuan_barang","harga_beli_rupiah","harga_beli_terakhir_rupiah","jenis_barang","status"]
    def harga_beli_rupiah(self, obj):
        locale.setlocale(locale.LC_NUMERIC, 'IND')
        rupiah = locale.format("%.*f", (2, obj.harga_beli), True)
        return "Rp. {}".format(rupiah)
    
    def harga_beli_terakhir_rupiah(self, obj):
        locale.setlocale(locale.LC_NUMERIC, 'IND')
        rupiah = locale.format("%.*f", (2, obj.harga_beli_terakhir), True)
        return "Rp. {}".format(rupiah)

admin.site.register(Barang,BarangAdmin)

#===========================================================================================================================
class KategoriBarangAdmin(admin.ModelAdmin):
    list_display = ["kode","name","status"]

admin.site.register(KategoriBarang,KategoriBarangAdmin)

#===========================================================================================================================
class PerusahaanAdmin(admin.ModelAdmin):
    list_display = ["kode","name","no_telfon","alamat","status"]

admin.site.register(Perusahaan,PerusahaanAdmin)

#===========================================================================================================================
class SatuanBarangAdmin(admin.ModelAdmin):
    list_display = ["kode","name","status"]

admin.site.register(SatuanBarang,SatuanBarangAdmin)

#===========================================================================================================================
class PoliklinikAdmin(admin.ModelAdmin):
    list_display = ["kode","name"]

admin.site.register(Poliklinik,PoliklinikAdmin)

#===========================================================================================================================
class UnitAdmin(admin.ModelAdmin):
    list_display = ["kode","name"]

admin.site.register(Unit,UnitAdmin)

#===========================================================================================================================
class BangsalAdmin(admin.ModelAdmin):
    list_display = ["kode","name","status"]

admin.site.register(Bangsal,BangsalAdmin)