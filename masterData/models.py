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

class Poliklinik(models.Model):
      kode=models.CharField(max_length=30,unique=True)
      name=models.CharField(max_length=50)
      class Meta:
            verbose_name="Poliklinik"
            verbose_name_plural = "Poliklinik"
      def __str__(self):
            return self.name

class Bangsal(models.Model):
      kode=models.CharField(max_length=30,unique=True)
      name=models.CharField(max_length=50)
      status=models.BooleanField()
      class Meta:
            verbose_name="Bangsal"
            verbose_name_plural = "Bangsal"
      def __str__(self):
            return self.name

class kategori_perawatan(models.Model):
      kode=models.CharField(max_length=30,unique=True)
      name=models.CharField(max_length=50)
      class Meta:
            verbose_name="Kategori Perawatan"
            verbose_name_plural = "Kategori Perawatan"
      def __str__(self):
            return self.name


class perawatan_rawat_jalan(models.Model):
      kode=models.CharField(max_length=30,unique=True)
      nama_perawatan=models.CharField(max_length=50)
      kategori = models.ForeignKey(kategori_perawatan,on_delete=models.RESTRICT,null=True,blank=True)
      status=models.BooleanField()
      class Meta:
            verbose_name="Perawatan Rawat Jalan"
            verbose_name_plural = "Perawatan Rawat Jalan"
      def __str__(self):
            return self.nama_perawatan