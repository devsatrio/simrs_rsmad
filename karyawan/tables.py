import django_tables2 as tables
from django_tables2 import TemplateColumn
from .models import Karyawan,BerkasKaryawan
from django_tables2.utils import A

# =========================================================================================================
class KaryawanTable(tables.Table):
    Aksi = TemplateColumn(template_code='<a href="{% url "karyawan:show" record.id %}" class="btn btn-warning btn-sm"><i class="fas fa-eye"></a>')

    class Meta:
        model=Karyawan

# =========================================================================================================
class BerkasSayaTable(tables.Table):
    Aksi = TemplateColumn(template_code='<a href="{% url "karyawan:berkas-saya-show" record.id %}" class="btn btn-warning btn-sm"><i class="fas fa-eye"></a>')
    class Meta:
        model=BerkasKaryawan
        fields = ("pk","nama_berkas", "kategori", "berkas","status_berkas", "verifikator","keterangan_verifikator")

# =========================================================================================================
class BerkasKaryawanTable(tables.Table):
    Aksi = TemplateColumn(template_code='<a href="{% url "karyawan:berkas-karyawan-show" record.id %}" class="btn btn-warning m-1 btn-sm"><i class="fas fa-eye"></i></a>')
    class Meta:
        model=BerkasKaryawan
        fields = ("pk","karyawan","nama_berkas", "kategori", "berkas","status_berkas", "verifikator","keterangan_verifikator")