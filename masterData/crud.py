from crudbuilder.abstract import BaseCrudBuilder
from .models import Agama,JenisKelamin,GolonganDarah,StatusNikah,StrataPendidikan,JenisPekerjaan,Asuransi,Poliklinik,Bangsal,kategori_perawatan,perawatan_rawat_jalan

class AgamaCrud(BaseCrudBuilder):
    model = Agama
    tables2_css_class = "table table-bordered table-condensed"
    login_required = True
    permission_required = True
    search_fields = ['name']
    tables2_fields = ('name',)
    custom_postfix_url = 'master-data-agama'
    permissions = {
        'list'  : 'masterData.view_agama',
        'create': 'masterData.add_agama',
        'detail': 'masterData.view_agama',
        'update': 'masterData.change_agama',
        'delete': 'masterData.delete_agama',
    }

class JenisKelaminCrud(BaseCrudBuilder):
    model = JenisKelamin
    tables2_css_class = "table table-bordered table-condensed"
    login_required = True
    permission_required = True
    search_fields = ['name']
    tables2_fields = ('name',)
    custom_postfix_url = 'master-data-jenis-kelamin'
    permissions = {
        'list'  : 'masterData.view_jeniskelamin',
        'create': 'masterData.add_jeniskelamin',
        'detail': 'masterData.view_jeniskelamin',
        'update': 'masterData.change_jeniskelamin',
        'delete': 'masterData.delete_jeniskelamin',
    }

class GolonganDarahCrud(BaseCrudBuilder):
    model = GolonganDarah
    tables2_css_class = "table table-bordered table-condensed"
    login_required = True
    search_fields = ['name']
    tables2_fields = ('name',)
    custom_postfix_url = 'master-data-golongan-darah'

class StatusNikahCrud(BaseCrudBuilder):
    model = StatusNikah
    tables2_css_class = "table table-bordered table-condensed"
    login_required = True
    search_fields = ['name']
    tables2_fields = ('name',)
    custom_postfix_url = 'master-data-status-nikah'

class StrataPendidikanCrud(BaseCrudBuilder):
    model = StrataPendidikan
    tables2_css_class = "table table-bordered table-condensed"
    login_required = True
    search_fields = ['name']
    tables2_fields = ('name',)
    custom_postfix_url = 'master-data-strata-pendidikan'

class JenisPekerjaanCrud(BaseCrudBuilder):
    model = JenisPekerjaan
    tables2_css_class = "table table-bordered table-condensed"
    login_required = True
    search_fields = ['name']
    tables2_fields = ('name',)
    custom_postfix_url = 'master-data-jenis-pekerjaan'

class AsuransiCrud(BaseCrudBuilder):
    model = Asuransi
    tables2_css_class = "table table-bordered table-condensed"
    login_required = True
    permission_required = True
    search_fields = ['name']
    tables2_fields = ('name',)
    custom_postfix_url = 'master-data-asuransi'
    permissions = {
        'list'  : 'masterData.view_asuransi',
        'create': 'masterData.add_asuransi',
        'detail': 'masterData.view_asuransi',
        'update': 'masterData.change_asuransi',
        'delete': 'masterData.delete_asuransi',
    }

class PoliklinikCrud(BaseCrudBuilder):
    model = Poliklinik
    tables2_css_class = "table table-bordered table-condensed"
    login_required = True
    search_fields = ['kode','name']
    tables2_fields = ('kode','name',)
    custom_postfix_url = 'master-data-poliklinik'

class BangsalCrud(BaseCrudBuilder):
    model = Bangsal
    tables2_css_class = "table table-bordered table-condensed"
    login_required = True
    search_fields = ['kode','name']
    tables2_fields = ('kode','name',)
    custom_postfix_url = 'master-data-bangsal'

class kategori_perawatanCrud(BaseCrudBuilder):
    model = kategori_perawatan
    tables2_css_class = "table table-bordered table-condensed"
    login_required = True
    search_fields = ['kode','name']
    tables2_fields = ('kode','name',)
    custom_postfix_url = 'master-data-kategori-perawatan'

class perawatan_rawat_jalanCrud(BaseCrudBuilder):
    model = perawatan_rawat_jalan
    tables2_css_class = "table table-bordered table-condensed"
    login_required = True
    search_fields = ['kode','nama_perawatan']
    tables2_fields = ('kode','nama_perawatan','kategori','status',)
    custom_postfix_url = 'master-data-perawatan-rawat-jalan'
