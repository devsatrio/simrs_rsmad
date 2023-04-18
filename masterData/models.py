from django.db import models

# Create your models here.
class Agama(models.Model):
    name=models.CharField(max_length=30)
    class Meta:
          verbose_name="Agama"
          verbose_name_plural = "Agama"
    def __str__(self):
            return self.name

class JenisKelamin(models.Model):
    name=models.CharField(max_length=30)
    class Meta:
          verbose_name="Jenis Kelamin"
          verbose_name_plural = "Jenis Kelamin"
    def __str__(self):
            return self.name

class GolonganDarah(models.Model):
    name=models.CharField(max_length=30)
    class Meta:
          verbose_name="Golongan Darah"
          verbose_name_plural = "Golongan Darah"
    def __str__(self):
            return self.name

class StatusNikah(models.Model):
    name=models.CharField(max_length=30)
    class Meta:
          verbose_name="Status Nikah"
          verbose_name_plural = "Status Nikah"
    def __str__(self):
            return self.name

class StrataPendidikan(models.Model):
    name=models.CharField(max_length=30)
    class Meta:
          verbose_name="Strata Pendidikan"
          verbose_name_plural = "Strata Pendidikan"
    def __str__(self):
            return self.name        
    
class JenisPekerjaan(models.Model):
    name=models.CharField(max_length=30)
    class Meta:
          verbose_name="Jenis Pekerjaan"
          verbose_name_plural = "Jenis Pekerjaan"
    def __str__(self):
            return self.name   

class Asuransi(models.Model):
    name=models.CharField(max_length=30)
    class Meta:
          verbose_name="Asuransi"
          verbose_name_plural = "Asuransi"
    def __str__(self):
            return self.name   