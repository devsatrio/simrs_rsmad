from django.db import models
from masterData.models import Penyakit,Prosedur
from frontoffice.models import registrasi
from karyawan.models import Karyawan
from datetime import datetime,date

        
class StatusDiagnosaChoices(models.TextChoices):
        primary = 'Primary', 'Primary'
        sekunder = 'Sekunder', 'Sekunder'

class StatusPeriksaChoices(models.TextChoices):
        ralan = 'RALAN', 'RALAN'
        ranap = 'RANAP', 'RANAP'

#===========================================================================================================================
class diagnosa(models.Model):
    no_rawat = models.ForeignKey(registrasi,on_delete=models.RESTRICT,null=True,blank=True)
    diagnosa = models.ForeignKey(Penyakit,on_delete=models.RESTRICT,null=True,blank=True)
    status = models.CharField(max_length=50,choices=StatusDiagnosaChoices.choices,default=StatusDiagnosaChoices.primary)
    diagnosa_dokter=models.TextField(max_length=300,blank=True,null=True)
    status_periksa = models.CharField(max_length=50,choices=StatusPeriksaChoices.choices,default=StatusPeriksaChoices.ralan)
    dokter = models.ForeignKey(Karyawan,on_delete=models.RESTRICT,related_name='dokter_pemberi_diagnosa',null=True,blank=True)
    created_by = models.ForeignKey(Karyawan,on_delete=models.RESTRICT,related_name='created_by_diagnosa',null=True,blank=True)
    created_at =models.DateTimeField(null=True,default=datetime.now,blank=True)

    class Meta:
        verbose_name="Diagnosa (ICD 10)"
        verbose_name_plural = "Diagnosa (ICD 10)"

    def __str__(self):
        return self.diagnosa_dokter

#===========================================================================================================================
class tindakan(models.Model):
    no_rawat = models.ForeignKey(registrasi,on_delete=models.RESTRICT,null=True,blank=True)
    tindakan = models.ForeignKey(Prosedur,on_delete=models.RESTRICT,null=True,blank=True)
    status = models.CharField(max_length=50,choices=StatusDiagnosaChoices.choices,default=StatusDiagnosaChoices.primary)
    tindakan_dokter=models.TextField(max_length=300,blank=True,null=True)
    status_periksa = models.CharField(max_length=50,choices=StatusPeriksaChoices.choices,default=StatusPeriksaChoices.ralan)
    dokter = models.ForeignKey(Karyawan,on_delete=models.RESTRICT,related_name='dokter_pemberi_tindakan',null=True,blank=True)
    created_by = models.ForeignKey(Karyawan,on_delete=models.RESTRICT,related_name='created_by_tindakan',null=True,blank=True)
    created_at =models.DateTimeField(null=True,default=datetime.now,blank=True)

    class Meta:
        verbose_name="Tindakan (ICD 9)"
        verbose_name_plural = "Tindakan (ICD 9)"

    def __str__(self):
        return self.tindakan_dokter
