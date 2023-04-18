from django.contrib import admin
from .models import pasien
from .forms import pasienForm

class pasienAdmin(admin.ModelAdmin):
    list_filter=("no_rkm_medis","nama","nip","jenis_kelamin","golongan_darah","agama")
    list_display = ("no_rkm_medis","nama","nip","jenis_kelamin","tgl_lahir","golongan_darah","agama","kecamatan")
    form = pasienForm
    class Media:
        js = (
            'js/chained-area.js',
        )

admin.site.register(pasien,pasienAdmin)
