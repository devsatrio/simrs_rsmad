from django.db import models
from django.contrib.auth.models import User
from masterData.models import Agama, GolonganDarah, JenisKelamin, StatusNikah

# Create your models here.
class StatusKaryawan(models.Model):
    name=models.CharField(max_length=30)
    class Meta:
          verbose_name="Status Karyawan"
          verbose_name_plural = "Status Karyawan"
    def __str__(self):
            return self.name
    
class Karyawan(models.Model):
    nama=models.CharField(max_length=30)
    nama_lengkap=models.CharField(max_length=200)
    user = models.OneToOneField(User,on_delete=models.RESTRICT,null=True,blank=True)
    status_karyawan = models.ForeignKey(StatusKaryawan,on_delete=models.RESTRICT,null=True)
    agama = models.ForeignKey(Agama,on_delete=models.RESTRICT,null=True,blank=True)
    jenis_kelamin = models.ForeignKey(JenisKelamin,on_delete=models.RESTRICT,null=True)
    golongan_darah = models.ForeignKey(GolonganDarah,on_delete=models.RESTRICT,null=True)
    status_nikah = models.ForeignKey(StatusNikah,on_delete=models.RESTRICT,null=True)
    class Meta:
          verbose_name="Karyawan"
          verbose_name_plural = "Karyawan"
    def __str__(self):
            return self.nama_lengkap
    