from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django_cleanup import cleanup
from django.core.validators import MinLengthValidator
from masterData.models import Agama, GolonganDarah, JenisKelamin, StatusNikah, Unit,StrataPendidikan,Unit

# =========================================================================================================
class StatusBerkasChoices(models.TextChoices):
      diajukan = 'Berkas Diajukan', 'Berkas Diajukan'
      berkas_ditolak = 'Berkas Ditolak', 'Berkas Ditolak'
      berkas_diterima = 'Berkas Diterima', 'Berkas Diterima'

# =========================================================================================================
class StatusKaryawan(models.Model):
    name=models.CharField(max_length=30)
    class Meta:
          verbose_name="Status Karyawan"
          verbose_name_plural = "Status Karyawan"
    def __str__(self):
            return self.name

# =========================================================================================================   
class GolonganKaryawan(models.Model):
      nama=models.CharField(max_length=40)
      keterangan=models.TextField(max_length=200,null=True,blank=True)
      class Meta:
            verbose_name="Golongan Karyawan"
            verbose_name_plural = "Golongan Karyawan"
      def __str__(self):
                  return self.nama

# =========================================================================================================
class JabatanKaryawan(models.Model):
      nama=models.CharField(max_length=40)
      keterangan=models.TextField(max_length=200,null=True,blank=True)
      class Meta:
            verbose_name="Jabatan Karyawan"
            verbose_name_plural = "Jabatan Karyawan"
      def __str__(self):
                  return self.nama

# =========================================================================================================
class KategoriBerkasKaryawan(models.Model):
      nama=models.CharField(max_length=40)
      class Meta:
            verbose_name="Kategori Berkas"
            verbose_name_plural = "Kategori Berkas"
      def __str__(self):
                  return self.nama

# =========================================================================================================
class JamKerja(models.Model):
      nama = models.CharField(max_length=200)
      jam_masuk =  models.TimeField()
      jam_pulang =  models.TimeField()
      lama_jam_kerja = models.IntegerField(null=True,blank=True)
      gunakan_aturan_jam=models.BooleanField()
      keterangan = models.TextField(max_length=200,null=True,blank=True)
      
      class Meta:
            verbose_name="Jam Kerja"
            verbose_name_plural = "Jam Kerja"
      def __str__(self):
                  return self.nama
      
# =========================================================================================================
@cleanup.select
class Karyawan(models.Model):
      kode=models.CharField(max_length=30,unique=True,validators=[
            MinLengthValidator(8, 'must contain at least 8 characters')
            ]
        )
      nik=models.CharField(max_length=30,null=True,blank=True)
      nama=models.CharField(max_length=30)
      nama_lengkap=models.CharField(max_length=200)
      no_telfon=models.CharField(max_length=30,null=True,blank=True)
      no_karyawan_tetap=models.CharField(max_length=30,null=True,blank=True)
      tempat_lahir=models.CharField(max_length=30,null=True,blank=True)
      tgl_lahir=models.DateField(max_length=30,null=True,blank=True)
      no_str=models.CharField(max_length=30,null=True,blank=True)
      tgl_berlaku_str=models.DateField(max_length=30,null=True,blank=True)
      no_sip=models.CharField(max_length=30,null=True,blank=True)
      tgl_berlaku_sip=models.DateField(max_length=30,null=True,blank=True)
      user = models.OneToOneField(User,on_delete=models.RESTRICT,null=True,blank=True)
      status_karyawan = models.ForeignKey(StatusKaryawan,on_delete=models.RESTRICT,null=True)
      agama = models.ForeignKey(Agama,on_delete=models.RESTRICT,null=True,blank=True)
      jenis_kelamin = models.ForeignKey(JenisKelamin,on_delete=models.RESTRICT,null=True)
      golongan_darah = models.ForeignKey(GolonganDarah,on_delete=models.RESTRICT,null=True)
      status_nikah = models.ForeignKey(StatusNikah,on_delete=models.RESTRICT,null=True)
      golongan_karyawan = models.ForeignKey(GolonganKaryawan,on_delete=models.RESTRICT,null=True,blank=True)
      jabatan_karyawan = models.ForeignKey(JabatanKaryawan,on_delete=models.RESTRICT,null=True,blank=True)
      unit = models.ForeignKey(Unit,on_delete=models.RESTRICT,null=True,blank=True)
      foto = models.ImageField(upload_to='karyawan/', blank=True,null=True)
      jam_kerja = models.ManyToManyField(JamKerja,blank=True)
      class Meta:
            verbose_name="Data Karyawan"
            verbose_name_plural = "Data Karyawan"
            permissions = [
                  ("cv_saya", "Can access cv saya"),
                  ("dashboard_admin_karyawan", "Can access dashboard admin karyawan"),
                  ("dashboard_karyawan", "Can access dashboard karyawan"),
            ]
      def __str__(self):
                  return self.nama_lengkap

# =========================================================================================================
@cleanup.select
class BerkasKaryawan(models.Model):
      karyawan = models.ForeignKey(Karyawan,on_delete=models.RESTRICT,null=True,blank=True)
      nama_berkas=models.CharField(max_length=200)
      kategori = models.ForeignKey(KategoriBerkasKaryawan,on_delete=models.RESTRICT,null=True,blank=True)
      berkas = models.FileField(upload_to='documents/', blank=True,null=True)
      verifikator = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.RESTRICT,null=True,blank=True)
      keterangan_verifikator = models.TextField(max_length=300,blank=True,null=True)
      status_berkas = models.CharField(max_length=50,choices=StatusBerkasChoices.choices,default=StatusBerkasChoices.diajukan)
      class Meta:
            verbose_name="Berkas Karyawan"
            verbose_name_plural = "Berkas Karyawan"
            permissions = [
                  ("berkas_saya", "Can access berkas saya"),
            ]
      def __str__(self):
                  return self.nama_berkas

# =========================================================================================================
class RiwayatPendidikanKaryawan(models.Model):
      karyawan = models.ForeignKey(Karyawan,on_delete=models.RESTRICT,null=True,blank=True)
      strata_pendidikan = models.ForeignKey(StrataPendidikan,on_delete=models.RESTRICT)
      nama_sekolah=models.CharField(max_length=80)
      tahun_lulus=models.CharField(max_length=10)
      berkas=models.ForeignKey(BerkasKaryawan,on_delete=models.RESTRICT,blank=True,null=True)
      class Meta:
            verbose_name="Riwayat Pendidikan Karyawan"
            verbose_name_plural = "Riwayat Pendidikan Karyawan"
            permissions = [
                  ("riwayat_pendidikan_saya", "Can access riwayat pendidikan saya"),
            ]
      def __str__(self):
                  return self.nama_sekolah

# =========================================================================================================
class AbsensiKaryawan(models.Model):
      karyawan = models.ForeignKey(Karyawan,on_delete=models.RESTRICT,null=True,blank=True)
      jam_kerja = models.ForeignKey(JamKerja,on_delete=models.RESTRICT,null=True,blank=True)
      tgl_absen=models.DateField(max_length=30,null=True,blank=True)
      jam_masuk_karyawan =  models.TimeField(null=True,blank=True)
      jam_pulang_karyawan =  models.TimeField(null=True,blank=True)
      lama_jam_kerja_karyawan = models.IntegerField(null=True,blank=True)
      class Meta:
            verbose_name="Absensi Karyawan"
            verbose_name_plural = "Absensi Karyawan"

      def __str__(self):
                  return str(self.tgl_absen)

# =========================================================================================================
class KarirKaryawan(models.Model):
      karyawan = models.ForeignKey(Karyawan,on_delete=models.RESTRICT,null=True,blank=True)
      unit = models.ForeignKey(Unit,on_delete=models.RESTRICT)
      jabatan = models.ForeignKey(JabatanKaryawan,on_delete=models.RESTRICT)
      tahun_menjabat=models.IntegerField()
      tahun_berhenti_menjabat=models.IntegerField(blank=True,null=True)
      berkas=models.ForeignKey(BerkasKaryawan,on_delete=models.RESTRICT,blank=True,null=True)
      class Meta:
            verbose_name="Karir Karyawan"
            verbose_name_plural = "Karir Karyawan"
            permissions = [
                  ("karir_saya", "Can access karir saya"),
            ]
      def __str__(self):
                  return self.unit.name

# =========================================================================================================
class PelatihanKaryawan(models.Model):
      karyawan = models.ForeignKey(Karyawan,on_delete=models.RESTRICT,null=True,blank=True)
      nama_pelatihan = models.CharField(max_length=200)
      tanggal_pelatihan=models.DateField()
      tahun_kegiatan=models.IntegerField()
      tahun_expired=models.IntegerField(blank=True,null=True)
      berkas=models.ForeignKey(BerkasKaryawan,on_delete=models.RESTRICT,blank=True,null=True)
      class Meta:
            verbose_name="Pelatihan Karyawan"
            verbose_name_plural = "Pelatihan Karyawan"
            permissions = [
                  ("pelatihan_saya", "Can access pelatihan saya"),
            ]
      def __str__(self):
                  return self.nama_pelatihan
