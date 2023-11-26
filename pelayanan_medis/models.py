from django.db import models
from masterData.models import perawatan_rawat_jalan,kategori_perawatan
from karyawan.models import Karyawan
from frontoffice.models import registrasi
from datetime import datetime,date

def getdetailtindakan(id_tindakan):
    tindakan = perawatan_rawat_jalan.objects.get(id=id_tindakan)
    return tindakan

#===========================================================================================================================
class perawatan_rawat_jalan_pasien(models.Model):
      no_rawat = models.ForeignKey(registrasi,on_delete=models.RESTRICT,null=True,blank=True)
      perawatan_rawat_jalan = models.ForeignKey(perawatan_rawat_jalan,on_delete=models.RESTRICT,null=True,blank=True)
      tgl_perawatan=models.DateTimeField(null=True,default=datetime.now,blank=True)
      dokter = models.ForeignKey(Karyawan,on_delete=models.RESTRICT,related_name='dokter_pelaksana_tindakan_rj',null=True,blank=True)
      petugas = models.ForeignKey(Karyawan,on_delete=models.RESTRICT,related_name='petugas_pelaksana_tindakan_rj',null=True,blank=True)
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
            verbose_name="Perawatan Rajal"
            verbose_name_plural = "Perawatan Rajal"

      def __str__(self):
            return self.nama_perawatan
      
      def save(self, *args, **kwargs):
            self.kategori=kategori_perawatan.objects.get(id=self.perawatan_rawat_jalan.kategori.id)
            self.nama_perawatan = self.perawatan_rawat_jalan.nama_perawatan
            self.biaya_material = self.perawatan_rawat_jalan.biaya_material
            self.biaya_bhp = self.perawatan_rawat_jalan.biaya_bhp
            self.biaya_dokter = self.perawatan_rawat_jalan.biaya_dokter
            self.biaya_perawat = self.perawatan_rawat_jalan.biaya_perawat
            self.biaya_kso = self.perawatan_rawat_jalan.biaya_kso
            self.biaya_manajemen = self.perawatan_rawat_jalan.biaya_manajemen
            self.biaya_rawat = self.perawatan_rawat_jalan.biaya_rawat
            self.total_biaya = self.perawatan_rawat_jalan.total_biaya
            super(perawatan_rawat_jalan_pasien, self).save(*args, **kwargs)