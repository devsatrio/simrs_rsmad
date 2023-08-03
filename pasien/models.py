from django.db import models
from masterData.models import JenisKelamin,GolonganDarah,Agama, JenisPekerjaan, StatusNikah, StrataPendidikan
from masterWilayah.models import negara, propinsi, kota, kecamatan, kelurahan
from django.db.models import Max
from datetime import datetime


def create_new_ref_number():
    last_pasien = pasien.objects.aggregate(Max('no_rkm_medis'))
    if last_pasien['no_rkm_medis__max'] is not None:
        final_pasien_number = int(last_pasien['no_rkm_medis__max'])+1
    else:
        final_pasien_number = 1
    final_pasien_string = str(final_pasien_number).zfill(6)
    return final_pasien_string

class pasien(models.Model):
    no_rkm_medis=models.CharField(max_length = 10,blank=True,editable=False,unique=True,default=create_new_ref_number)
    nama=models.CharField(max_length=200)
    no_ktp=models.CharField(max_length=50,null=True,blank=False)
    jenis_kelamin = models.ForeignKey(JenisKelamin,on_delete=models.RESTRICT,null=False)
    tgl_lahir = models.DateField(null=False)
    golongan_darah=models.ForeignKey(GolonganDarah,on_delete=models.RESTRICT,null=True,blank=True)
    agama = models.ForeignKey(Agama,on_delete=models.RESTRICT,null=True,blank=True)
    jenis_pekerjaan = models.ForeignKey(JenisPekerjaan,on_delete=models.RESTRICT,null=True,blank=True)
    status_nikah = models.ForeignKey(StatusNikah,on_delete=models.RESTRICT,null=True,blank=True)
    strata_pendidikan = models.ForeignKey(StrataPendidikan,on_delete=models.RESTRICT,null=True,blank=True)
    tgl_daftar = models.DateField(null=True,default=datetime.now,blank=True)
    no_telfon=models.CharField(max_length=50,null=True,blank=False)
    nip=models.CharField(max_length=50,null=True,blank=True)
    negara = models.ForeignKey(negara,on_delete=models.RESTRICT,null=True,blank=True)
    propinsi = models.ForeignKey(propinsi,on_delete=models.RESTRICT,null=True,blank=True)
    kota = models.ForeignKey(kota,on_delete=models.RESTRICT,null=True,blank=True)
    kecamatan = models.ForeignKey(kecamatan,on_delete=models.RESTRICT,null=True,blank=True)
    kelurahan = models.ForeignKey(kelurahan,on_delete=models.RESTRICT,null=True,blank=True)

    class Meta:
        verbose_name="Data Pasien"
        verbose_name_plural ="Data Pasien"

    def __str__(self):
        return self.nama
