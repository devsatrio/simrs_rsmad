from django.db import models

class negara(models.Model):
    iso=models.CharField(max_length=50)
    name=models.CharField(max_length=80)
    nicename=models.CharField(max_length=80)
    iso3=models.CharField(max_length=10)
    numcode=models.IntegerField()
    phonecode=models.IntegerField()
    class Meta:
        verbose_name="Negara"
        verbose_name_plural="Negara"
    
    def __str__(self):
        return self.name

class propinsi(models.Model):
    name=models.CharField(max_length=80)
    negara = models.ForeignKey(negara,on_delete=models.RESTRICT,null=True)
    class Meta:
        verbose_name="Propinsi"
        verbose_name_plural="Propinsi"
    
    def __str__(self):
        return self.name

class kota(models.Model):
    name=models.CharField(max_length=80)
    propinsi = models.ForeignKey(propinsi,on_delete=models.RESTRICT,null=True)
    class Meta:
        verbose_name="Kota"
        verbose_name_plural="Kota"
    
    def __str__(self):
        return self.name
    
class kecamatan(models.Model):
    name=models.CharField(max_length=80)
    kota = models.ForeignKey(kota,on_delete=models.RESTRICT,null=True)
    class Meta:
        verbose_name="Kecamatan"
        verbose_name_plural="Kecamatan"
    
    def __str__(self):
        return self.name

class kelurahan(models.Model):
    name=models.CharField(max_length=80)
    kecamatan = models.ForeignKey(kecamatan,on_delete=models.RESTRICT,null=True)
    class Meta:
        verbose_name="Kelurahan"
        verbose_name_plural="Kelurahan"
    
    def __str__(self):
        return self.name