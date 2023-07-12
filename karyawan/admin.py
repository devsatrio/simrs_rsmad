from django.contrib import admin
from django.utils.html import format_html
from .forms import RiwayatPedidikanKaryawanAdminForm,KarirKaryawanAdminForm,PelatihanKaryawanAdminForm
from .models import KarirKaryawan,StatusKaryawan,Karyawan,JabatanKaryawan,GolonganKaryawan,KategoriBerkasKaryawan,BerkasKaryawan,RiwayatPendidikanKaryawan,PelatihanKaryawan, JamKerja
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
# Register your models here.


#===========================================================================================================================
class PelatihanKaryawanAdmin(admin.ModelAdmin):
    list_filter = ["karyawan"]
    list_display = ('karyawan','nama_pelatihan','tanggal_pelatihan','tahun_kegiatan','tahun_expired','berkas','nama_berkas')
    form = PelatihanKaryawanAdminForm
    class Media:
        js = (
            'js/chained-berkas.js',
        )
    def nama_berkas(self, obj):
        if obj.berkas:
            # return format_html("<a href='%s' download>Download</a>" % (obj.berkas.berkas.url,))
            return format_html("<a href='%s' target='blank'>Download</a>" % (obj.berkas.berkas.url,))
        else:
            return "No attachment"
    nama_berkas.allow_tags = True
    nama_berkas.short_description = 'File Download'

admin.site.register(PelatihanKaryawan, PelatihanKaryawanAdmin)

#===========================================================================================================================
class KarirKaryawanAdmin(admin.ModelAdmin):
    list_filter = ["karyawan"]
    list_display = ('karyawan','unit','jabatan','tahun_menjabat','tahun_berhenti_menjabat','berkas','nama_berkas')
    form = KarirKaryawanAdminForm
    class Media:
        js = (
            'js/chained-berkas.js',
        )
    def nama_berkas(self, obj):
        if obj.berkas:
            # return format_html("<a href='%s' download>Download</a>" % (obj.berkas.berkas.url,))
            return format_html("<a href='%s' target='blank'>Download</a>" % (obj.berkas.berkas.url,))
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
            return format_html("<a href='%s' target='blank' >Download</a>" % (obj.berkas.berkas.url,))
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
class JamKerjaAdmin(admin.ModelAdmin):
    fields = ['nama','jam_masuk','jam_pulang','keterangan']
    list_display = ('nama','jam_masuk','jam_pulang','keterangan')

admin.site.register(JamKerja, JamKerjaAdmin)

#===========================================================================================================================
class KategoriBerkasKaryawanAdmin(admin.ModelAdmin):
    fields = ['nama']

admin.site.register(KategoriBerkasKaryawan, KategoriBerkasKaryawanAdmin)

#===========================================================================================================================
class BerkasKaryawanAdmin(admin.ModelAdmin):
    list_display = ('karyawan','nama_berkas','kategori','berkas','verifikator','keterangan_verifikator','status_berkas')

admin.site.register(BerkasKaryawan, BerkasKaryawanAdmin)

#===========================================================================================================================

def change_no_telp_action(modeladmin, request, queryset):
    for Karyawan in queryset:
        print(Karyawan.user)
        if(Karyawan.user is None):
            User.objects.create_user(username=Karyawan.kode,password=Karyawan.kode)
            my_group = Group.objects.get(name='Karyawan') 
            my_group.user_set.add(User.objects.get(username=Karyawan.kode))
            Karyawan.user = User.objects.get(username=Karyawan.kode)
            Karyawan.save()
change_no_telp_action.short_description = 'Generate Akun Karyawan'

class KaryawanAdmin(admin.ModelAdmin):
    list_display = ("kode","nama","nik","no_telfon", "nama_lengkap", "user","status_karyawan","agama","jenis_kelamin","golongan_darah","status_nikah","golongan_karyawan","jabatan_karyawan","unit",)
    list_filter = ["nama_lengkap","status_karyawan","golongan_karyawan","jabatan_karyawan"]
    actions = [change_no_telp_action,]
admin.site.register(Karyawan, KaryawanAdmin)
