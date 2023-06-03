from django.contrib import admin
from django.utils.html import format_html
from .forms import RiwayatPedidikanKaryawanAdminForm
from .models import KarirKaryawan,StatusKaryawan,Karyawan,JabatanKaryawan,GolonganKaryawan,KategoriBerkasKaryawan,BerkasKaryawan,RiwayatPendidikanKaryawan
# Register your models here.


#===========================================================================================================================
class KarirKaryawanAdmin(admin.ModelAdmin):
    list_filter = ["karyawan"]
    list_display = ('karyawan','unit','jabatan','tahun_menjabat','tahun_berhenti_menjabat','berkas','nama_berkas')
    def nama_berkas(self, obj):
        if obj.berkas:
            return format_html("<a href='%s' download>Download</a>" % (obj.berkas.berkas.url,))
        else:
            return "No attachment"
    nama_berkas.allow_tags = True
    nama_berkas.short_description = 'File Download'

admin.site.register(KarirKaryawan, KarirKaryawanAdmin)

#===========================================================================================================================
class RiwayatPendidikanKaryawanAdmin(admin.ModelAdmin):
    list_filter = ["nama_sekolah"]
    list_display = ('karyawan','strata_pendidikan','nama_sekolah','tahun_lulus','berkas','nama_berkas')
    form = RiwayatPedidikanKaryawanAdminForm
    class Media:
        js = (
            'js/chained-berkas.js',
        )
    def nama_berkas(self, obj):
        if obj.berkas:
            return format_html("<a href='%s' download>Download</a>" % (obj.berkas.berkas.url,))
        else:
            return "No attachment"
    nama_berkas.allow_tags = True
    nama_berkas.short_description = 'File Download'

admin.site.register(RiwayatPendidikanKaryawan, RiwayatPendidikanKaryawanAdmin)

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
    list_display = ('karyawan','nama_berkas','kategori','berkas','verifikator','keterangan_verifikator','status_berkas')

admin.site.register(BerkasKaryawan, BerkasKaryawanAdmin)

#===========================================================================================================================
class KaryawanAdmin(admin.ModelAdmin):
    list_display = ("nama", "nama_lengkap", "user","status_karyawan","agama","jenis_kelamin","golongan_darah","status_nikah","golongan_karyawan","jabatan_karyawan","unit")
    list_filter = ["nama_lengkap","status_karyawan","golongan_karyawan","jabatan_karyawan"]
admin.site.register(Karyawan, KaryawanAdmin)
