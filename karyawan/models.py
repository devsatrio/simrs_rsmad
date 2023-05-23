from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from masterData.models import Agama, GolonganDarah, JenisKelamin, StatusNikah, Unit

# Create your models here.
class StatusKaryawan(models.Model):
    name=models.CharField(max_length=30)
    class Meta:
          verbose_name="Status Karyawan"
          verbose_name_plural = "Status Karyawan"
    def __str__(self):
            return self.name
    
class GolonganKaryawan(models.Model):
      nama=models.CharField(max_length=40)
      keterangan=models.TextField(max_length=200,null=True,blank=True)
      class Meta:
            verbose_name="Golongan Karyawan"
            verbose_name_plural = "Golongan Karyawan"
      def __str__(self):
                  return self.nama

class JabatanKaryawan(models.Model):
      nama=models.CharField(max_length=40)
      keterangan=models.TextField(max_length=200,null=True,blank=True)
      class Meta:
            verbose_name="Jabatan Karyawan"
            verbose_name_plural = "Jabatan Karyawan"
      def __str__(self):
                  return self.nama

class KategoriBerkasKaryawan(models.Model):
      nama=models.CharField(max_length=40)
      class Meta:
            verbose_name="Kategori Berkas"
            verbose_name_plural = "Kategori Berkas"
      def __str__(self):
                  return self.nama

class Karyawan(models.Model):
    nama=models.CharField(max_length=30)
    nama_lengkap=models.CharField(max_length=200)
    user = models.OneToOneField(User,on_delete=models.RESTRICT,null=True,blank=True)
    status_karyawan = models.ForeignKey(StatusKaryawan,on_delete=models.RESTRICT,null=True)
    agama = models.ForeignKey(Agama,on_delete=models.RESTRICT,null=True,blank=True)
    jenis_kelamin = models.ForeignKey(JenisKelamin,on_delete=models.RESTRICT,null=True)
    golongan_darah = models.ForeignKey(GolonganDarah,on_delete=models.RESTRICT,null=True)
    status_nikah = models.ForeignKey(StatusNikah,on_delete=models.RESTRICT,null=True)
    golongan_karyawan = models.ForeignKey(GolonganKaryawan,on_delete=models.RESTRICT,null=True,blank=True)
    jabatan_karyawan = models.ForeignKey(JabatanKaryawan,on_delete=models.RESTRICT,null=True,blank=True)
    unit = models.ForeignKey(Unit,on_delete=models.RESTRICT,null=True,blank=True)
    class Meta:
          verbose_name="Karyawan"
          verbose_name_plural = "Karyawan"
    def __str__(self):
            return self.nama_lengkap

class BerkasKaryawan(models.Model):
      karyawan = models.ForeignKey(Karyawan,on_delete=models.RESTRICT,null=True,blank=True)
      nama_berkas=models.CharField(max_length=200)
      kategori = models.ForeignKey(KategoriBerkasKaryawan,on_delete=models.RESTRICT,null=True,blank=True)
      berkas = models.FileField(upload_to='documents/', blank=True,null=True)
      verifikator = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.RESTRICT,null=True,blank=True)
      keterangan_verifikator = models.TextField(max_length=300,blank=True,null=True)
      class Meta:
            verbose_name="Berkas Karyawan"
            verbose_name_plural = "Berkas Karyawan"
            permissions = [
                  ("verif_berkas", "Can verif the status of berkas"),
            ]
      def __str__(self):
                  return self.nama_berkas

    