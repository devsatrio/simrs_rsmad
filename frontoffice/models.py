
from django.db import models
from karyawan.models import Karyawan
from pasien.models import pasien
from masterData.models import Poliklinik,Asuransi
from django.db.models import Max
from datetime import datetime,date

class StatusPeriksaChoices(models.TextChoices):
        ralan = 'RALAN', 'RALAN'
        ranap = 'RANAP', 'RANAP'
        
class StatusBayarChoices(models.TextChoices):
        sudah_bayar = 'Sudah Bayar', 'Sudah Bayar'
        belum_bayar = 'Belum Bayar', 'Belum Bayar'

def GenerateNomorAntrian(poli):
    last_number = registrasi.objects.filter(poliklinik_id=poli).filter(tgl_registrasi=date.today()).aggregate(Max('no_registrasi'))

    if last_number['no_registrasi__max'] is not None:
        final_number = int(last_number['no_registrasi__max'])+1
    else:
        final_number = 1

    final_antrian_number = str(final_number).zfill(4)
    return final_antrian_number

def GenerateNomorRawat():
    today = date.today()
    last_number = registrasi.objects.filter(tgl_registrasi=date.today()).aggregate(Max('no_rawat'))
    
    if last_number['no_rawat__max'] is not None:
        last_number_split = last_number['no_rawat__max'].split("/")
        adding_number = int(last_number_split[3])+1
        final_number = str(today.year)+'/'+str(today.month).zfill(2)+'/'+str(today.day)+'/'+ str(adding_number).zfill(6)

    else:
        final_number = str(today.year)+'/'+str(today.month).zfill(2)+'/'+str(today.day)+'/000001'

    return final_number

class registrasi(models.Model):
    no_rawat=models.CharField(max_length=50,blank=True,null=True,editable=True)
    no_registrasi=models.CharField(max_length = 10,blank=True,null=True,editable=True)
    tgl_registrasi=models.DateField(null=True,default=datetime.now,blank=True)
    jam_registrasi = models.TimeField(null=True,default=datetime.now,blank=True)
    dokter = models.ForeignKey(Karyawan,on_delete=models.RESTRICT)
    pasien = models.ForeignKey(pasien,on_delete=models.RESTRICT,to_field="no_rkm_medis")
    poliklinik = models.ForeignKey(Poliklinik,on_delete=models.RESTRICT)
    penanggung_jawab_pasien = models.CharField(max_length=50)
    status_periksa = models.CharField(max_length=50,choices=StatusPeriksaChoices.choices,default=StatusPeriksaChoices.ralan)
    asuransi_pasien = models.ForeignKey(Asuransi,on_delete=models.RESTRICT)

    class Meta:
        verbose_name="Registrasi Pasien"
        verbose_name_plural = "Registrasi Pasien"

    def __str__(self):
        return self.no_rawat

    def save(self, *args, **kwargs):

        #membedakan antara save atau update
        if not self.id:
            self.no_registrasi=GenerateNomorAntrian(self.poliklinik)
            self.no_rawat=GenerateNomorRawat()

        super(registrasi, self).save(*args, **kwargs)