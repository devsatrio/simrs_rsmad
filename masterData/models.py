from django.db import models

# =========================================================================================================
class JenisBarang(models.TextChoices):
      logistik_rt = 'Logistik RT', 'Logistik RT'
      logistik_gizi = 'Logistik Gizi', 'Logistik Gizi'

#===========================================================================================================================
class Agama(models.Model):
    name=models.CharField(max_length=30)
    class Meta:
          verbose_name="Agama"
          verbose_name_plural = "Agama"
    def __str__(self):
            return self.name

#===========================================================================================================================
class JenisKelamin(models.Model):
    name=models.CharField(max_length=30)
    class Meta:
          verbose_name="Jenis Kelamin"
          verbose_name_plural = "Jenis Kelamin"
    def __str__(self):
            return self.name

#===========================================================================================================================
class GolonganDarah(models.Model):
    name=models.CharField(max_length=30)
    class Meta:
          verbose_name="Golongan Darah"
          verbose_name_plural = "Golongan Darah"
    def __str__(self):
            return self.name

#===========================================================================================================================
class StatusNikah(models.Model):
    name=models.CharField(max_length=30)
    class Meta:
          verbose_name="Status Nikah"
          verbose_name_plural = "Status Nikah"
    def __str__(self):
            return self.name

#===========================================================================================================================
class StrataPendidikan(models.Model):
    name=models.CharField(max_length=30)
    class Meta:
          verbose_name="Strata Pendidikan"
          verbose_name_plural = "Strata Pendidikan"
    def __str__(self):
            return self.name        

#===========================================================================================================================
class JenisPekerjaan(models.Model):
    name=models.CharField(max_length=30)
    class Meta:
          verbose_name="Jenis Pekerjaan"
          verbose_name_plural = "Jenis Pekerjaan"
    def __str__(self):
            return self.name   

#===========================================================================================================================
class Asuransi(models.Model):
    name=models.CharField(max_length=30)
    class Meta:
          verbose_name="Asuransi"
          verbose_name_plural = "Asuransi"
    def __str__(self):
            return self.name   

#===========================================================================================================================
class Poliklinik(models.Model):
      kode=models.CharField(max_length=30,unique=True)
      name=models.CharField(max_length=50)
      class Meta:
            verbose_name="Poliklinik"
            verbose_name_plural = "Poliklinik"
      def __str__(self):
            return self.name

#===========================================================================================================================
class Unit(models.Model):
      kode=models.CharField(max_length=30,unique=True)
      name=models.CharField(max_length=50)
      class Meta:
            verbose_name="Unit"
            verbose_name_plural = "Unit"
      def __str__(self):
            return self.name

#===========================================================================================================================
class Bangsal(models.Model):
      kode=models.CharField(max_length=30,unique=True)
      name=models.CharField(max_length=50)
      status=models.BooleanField()
      class Meta:
            verbose_name="Bangsal"
            verbose_name_plural = "Bangsal"
      def __str__(self):
            return self.name

#===========================================================================================================================
class Ruangan(models.Model):
      kode=models.CharField(max_length=30,unique=True)
      name=models.CharField(max_length=50)
      bangsal = models.ForeignKey(Bangsal,on_delete=models.RESTRICT,null=True,blank=True)
      status=models.BooleanField()
      class Meta:
            verbose_name="Ruangan"
            verbose_name_plural = "Ruangan"
      def __str__(self):
            return self.name

#===========================================================================================================================
class RuanganUnit(models.Model):
      unit = models.ForeignKey(Unit,on_delete=models.RESTRICT,null=True,blank=True)
      ruangan = models.ForeignKey(Ruangan,on_delete=models.RESTRICT,null=True,blank=True)
      class Meta:
            verbose_name="Ruangan Unit"
            verbose_name_plural = "Ruangan Unit"
      def __str__(self):
            return self.ruangan.name

#===========================================================================================================================
class kategori_perawatan(models.Model):
      kode=models.CharField(max_length=30,unique=True)
      name=models.CharField(max_length=50)
      class Meta:
            verbose_name="Kategori Perawatan"
            verbose_name_plural = "Kategori Perawatan"
      def __str__(self):
            return self.name

#===========================================================================================================================
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

#===========================================================================================================================
class SatuanBarang(models.Model):
      kode=models.CharField(max_length=30,unique=True)
      name=models.CharField(max_length=50)
      status=models.BooleanField()
      class Meta:
            verbose_name="Satuan Barang"
            verbose_name_plural = "Satuan Barang"
      def __str__(self):
            return self.name

#===========================================================================================================================
class KategoriBarang(models.Model):
      kode=models.CharField(max_length=30,unique=True)
      name=models.CharField(max_length=50)
      status=models.BooleanField()
      class Meta:
            verbose_name="Kategori Barang"
            verbose_name_plural = "Kategori Barang"
      def __str__(self):
            return self.name

#===========================================================================================================================
class Barang(models.Model):
      kode=models.CharField(max_length=30,unique=True)
      name=models.CharField(max_length=50)
      kategori_barang = models.ForeignKey(KategoriBarang,on_delete=models.RESTRICT,null=True,blank=True)
      stok = models.IntegerField(null=True,blank=True)
      satuan_barang = models.ForeignKey(SatuanBarang,on_delete=models.RESTRICT,null=True,blank=True)
      harga_beli = models.IntegerField(null=True,blank=True)
      harga_beli_terakhir = models.IntegerField(null=True,blank=True)
      jenis_barang = models.CharField(max_length=50,choices=JenisBarang.choices,default=JenisBarang.logistik_rt)
      status=models.BooleanField()
      class Meta:
            verbose_name="Barang"
            verbose_name_plural = "Barang"
      def __str__(self):
            return self.name

#===========================================================================================================================
class Perusahaan(models.Model):
      kode=models.CharField(max_length=30,unique=True)
      name=models.CharField(max_length=50)
      no_telfon=models.CharField(max_length=30,null=True,blank=True)
      alamat = models.TextField(max_length=300,blank=True,null=True)
      status=models.BooleanField()
      class Meta:
            verbose_name="Perusahaan"
            verbose_name_plural = "Perusahaan"
      def __str__(self):
            return self.name