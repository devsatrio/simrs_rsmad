import django_tables2 as tables
from django_tables2 import TemplateColumn
from .models import Karyawan,BerkasKaryawan,KarirKaryawan,RiwayatPendidikanKaryawan,PelatihanKaryawan
from django_tables2.utils import A
import itertools

# =========================================================================================================
class PelatihanSayaTable(tables.Table):
    no = tables.Column(empty_values=(), orderable=False)
    Aksi = TemplateColumn(template_code='<a href="{% url "karyawan:pelatihan-saya-show" record.id %}" class="btn btn-warning btn-sm"><i class="fas fa-eye"></a>')

    class Meta:
        model=PelatihanKaryawan
        sequence = ("no",)
        exclude = ("id","karyawan" )
    def render_no(self):
        self.row_no = getattr(self, 'row_no', itertools.count(self.page.start_index()))
        return next(self.row_no)

# =========================================================================================================
class PelatihanKaryawanTable(tables.Table):
    no = tables.Column(empty_values=(), orderable=False)
    Aksi = TemplateColumn(template_code='<a href="{% url "karyawan:pelatihan-karyawan-show" record.id %}" class="btn btn-warning btn-sm"><i class="fas fa-eye"></a>')

    class Meta:
        model=PelatihanKaryawan
        sequence = ("no",)
        exclude = ("id", )
    def render_no(self):
        self.row_no = getattr(self, 'row_no', itertools.count(self.page.start_index()))
        return next(self.row_no)
    
# =========================================================================================================
class RiwayatPendidikanSayaTable(tables.Table):
    no = tables.Column(empty_values=(), orderable=False)
    Aksi = TemplateColumn(template_code='<a href="{% url "karyawan:riwayat-pendidikan-saya-show" record.id %}" class="btn btn-warning btn-sm"><i class="fas fa-eye"></a>')

    class Meta:
        model=RiwayatPendidikanKaryawan
        sequence = ("no",)
        exclude = ("id","karyawan" )
    def render_no(self):
        self.row_no = getattr(self, 'row_no', itertools.count(self.page.start_index()))
        return next(self.row_no)

# =========================================================================================================
class RiwayatPendidikanKaryawanTable(tables.Table):
    no = tables.Column(empty_values=(), orderable=False)
    Aksi = TemplateColumn(template_code='<a href="{% url "karyawan:riwayat-pendidikan-karyawan-show" record.id %}" class="btn btn-warning btn-sm"><i class="fas fa-eye"></a>')

    class Meta:
        model=RiwayatPendidikanKaryawan
        sequence = ("no",)
        exclude = ("id", )
    def render_no(self):
        self.row_no = getattr(self, 'row_no', itertools.count(self.page.start_index()))
        return next(self.row_no)
    
# =========================================================================================================
class KarirSayaTable(tables.Table):
    no = tables.Column(empty_values=(), orderable=False)
    Aksi = TemplateColumn(template_code='<a href="{% url "karyawan:karir-saya-show" record.id %}" class="btn btn-warning btn-sm"><i class="fas fa-eye"></a>')

    class Meta:
        model=KarirKaryawan
        sequence = ("no",)
        exclude = ("id","karyawan" )
    def render_no(self):
        self.row_no = getattr(self, 'row_no', itertools.count(self.page.start_index()))
        return next(self.row_no)
        
# =========================================================================================================
class KarirKaryawanTable(tables.Table):
    no = tables.Column(empty_values=(), orderable=False)
    Aksi = TemplateColumn(template_code='<a href="{% url "karyawan:karir-karyawan-show" record.id %}" class="btn btn-warning btn-sm"><i class="fas fa-eye"></a>')

    class Meta:
        model=KarirKaryawan
        sequence = ("no",)
        exclude = ("id", )
    def render_no(self):
        self.row_no = getattr(self, 'row_no', itertools.count(self.page.start_index()))
        return next(self.row_no)

# =========================================================================================================
class KaryawanTable(tables.Table):
    no = tables.Column(empty_values=(), orderable=False)
    Aksi = TemplateColumn(template_code='<a href="{% url "karyawan:show" record.id %}" class="btn btn-warning btn-sm"><i class="fas fa-eye"></a>', orderable=False)

    class Meta:
        model=Karyawan
        sequence = ("Aksi","no","kode","nik", "nama",)
        exclude = ("id", "foto")
    def render_no(self):
        self.row_no = getattr(self, 'row_no', itertools.count(self.page.start_index()))
        return next(self.row_no)

# =========================================================================================================
class BerkasSayaTable(tables.Table):
    no = tables.Column(empty_values=(), orderable=False)
    Aksi = TemplateColumn(template_code='<a href="{% url "karyawan:berkas-saya-show" record.id %}" class="btn btn-warning btn-sm"><i class="fas fa-eye"></a>')
    class Meta:
        model=BerkasKaryawan
        fields = ("nama_berkas", "kategori", "berkas","status_berkas", "verifikator","keterangan_verifikator")
        sequence = ("no",)
    def render_no(self):
        self.row_no = getattr(self, 'row_no', itertools.count(self.page.start_index()))
        return next(self.row_no)

# =========================================================================================================
class BerkasKaryawanTable(tables.Table):
    no = tables.Column(empty_values=(), orderable=False)
    Aksi = TemplateColumn(template_code='<a href="{% url "karyawan:berkas-karyawan-show" record.id %}" class="btn btn-warning m-1 btn-sm"><i class="fas fa-eye"></i></a>')
    class Meta:
        model=BerkasKaryawan
        fields = ("karyawan","nama_berkas", "kategori", "berkas","status_berkas", "verifikator","keterangan_verifikator")
        sequence = ("no",)
    def render_no(self):
        self.row_no = getattr(self, 'row_no', itertools.count(self.page.start_index()))
        return next(self.row_no)