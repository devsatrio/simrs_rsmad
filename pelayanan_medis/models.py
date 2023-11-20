from django.db import models
from masterData.models import perawatan_rawat_jalan,kategori_perawatan
from karyawan.models import Karyawan
from frontoffice.models import registrasi



#===========================================================================================================================
class perawatan_rawat_jalan_pasien(models.Model):
      no_rawat = models.ForeignKey(registrasi,on_delete=models.RESTRICT,null=True,blank=True)
      perawatan_rawat_jalan = models.ForeignKey(perawatan_rawat_jalan,on_delete=models.RESTRICT,null=True,blank=True)
      kategori = models.ForeignKey(kategori_perawatan,on_delete=models.RESTRICT,null=True,blank=True)
      nama_perawatan=models.CharField(max_length=50,null=True,blank=True)
      biaya_material = models.IntegerField(null=True,blank=True)
      biaya_bhp = models.IntegerField(null=True,blank=True)
      biaya_dokter = models.IntegerField(null=True,blank=True)
      biaya_perawat = models.IntegerField(null=True,blank=True)
      biaya_kso = models.IntegerField(null=True,blank=True)
      biaya_manajemen = models.IntegerField(null=True,blank=True)
      biaya_rawat = models.IntegerField(null=True,blank=True)
      total_biaya = models.IntegerField(null=True,blank=True)
      class Meta:
            verbose_name="Perawatan Rawat Jalan Pasien"
            verbose_name_plural = "Perawatan Rawat Jalan Pasien"
      def __str__(self):
            return self.nama_perawatan