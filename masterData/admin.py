from django.contrib import admin
from .models import Agama,GolonganDarah,JenisKelamin,StatusNikah,JenisPekerjaan, StrataPendidikan, Asuransi

# Register your models here.

admin.site.register(Agama)
admin.site.register(GolonganDarah)
admin.site.register(JenisKelamin)
admin.site.register(StatusNikah)
admin.site.register(JenisPekerjaan)
admin.site.register(StrataPendidikan)
admin.site.register(Asuransi)