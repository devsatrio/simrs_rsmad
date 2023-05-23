from crudbuilder.abstract import BaseCrudBuilder
from .models import Agama,JenisKelamin,GolonganDarah,StatusNikah,StrataPendidikan,JenisPekerjaan,Asuransi,Poliklinik,Bangsal,kategori_perawatan,perawatan_rawat_jalan,Unit

class UnitCrud(BaseCrudBuilder):
    model = Unit
    tables2_css_class = "table table-bordered table-condensed"
    login_required = True
    permission_required = True
    search_fields = ['kode','name']
    tables2_fields = ('kode','name')
    custom_postfix_url = 'master-data-unit'
    permissions = {
        'list'  : 'masterData.view_unit',
        'create': 'masterData.add_unit',
        'detail': 'masterData.view_unit',
        'update': 'masterData.change_unit',
        'delete': 'masterData.delete_unit',
    }
    
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
    permission_required = True
    search_fields = ['name']
    tables2_fields = ('name',)
    custom_postfix_url = 'master-data-golongan-darah'
    permissions = {
        'list'  : 'masterData.view_golongandarah',
        'create': 'masterData.add_golongandarah',
        'detail': 'masterData.view_golongandarah',
        'update': 'masterData.change_golongandarah',
        'delete': 'masterData.delete_golongandarah',
    }

class StatusNikahCrud(BaseCrudBuilder):
    model = StatusNikah
    tables2_css_class = "table table-bordered table-condensed"
    login_required = True
    permission_required = True
    search_fields = ['name']
    tables2_fields = ('name',)
    custom_postfix_url = 'master-data-status-nikah'
    permissions = {
        'list'  : 'masterData.view_statusnikah',
        'create': 'masterData.add_statusnikah',
        'detail': 'masterData.view_statusnikah',
        'update': 'masterData.change_statusnikah',
        'delete': 'masterData.delete_statusnikah',
    }

class StrataPendidikanCrud(BaseCrudBuilder):
    model = StrataPendidikan
    tables2_css_class = "table table-bordered table-condensed"
    login_required = True
    permission_required = True
    search_fields = ['name']
    tables2_fields = ('name',)
    custom_postfix_url = 'master-data-strata-pendidikan'
    permissions = {
        'list'  : 'masterData.view_statusnikah',
        'create': 'masterData.add_statusnikah',
        'detail': 'masterData.view_statusnikah',
        'update': 'masterData.change_statusnikah',
        'delete': 'masterData.delete_statusnikah',
    }

class JenisPekerjaanCrud(BaseCrudBuilder):
    model = JenisPekerjaan
    tables2_css_class = "table table-bordered table-condensed"
    login_required = True
    permission_required = True
    search_fields = ['name']
    tables2_fields = ('name',)
    custom_postfix_url = 'master-data-jenis-pekerjaan'
    permissions = {
        'list'  : 'masterData.view_jenispekerjaan',
        'create': 'masterData.add_jenispekerjaan',
        'detail': 'masterData.view_jenispekerjaan',
        'update': 'masterData.change_jenispekerjaan',
        'delete': 'masterData.delete_jenispekerjaan',
    }

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
    permission_required = True
    search_fields = ['kode','name']
    tables2_fields = ('kode','name',)
    custom_postfix_url = 'master-data-poliklinik'
    permissions = {
        'list'  : 'masterData.view_poliklinik',
        'create': 'masterData.add_poliklinik',
        'detail': 'masterData.view_poliklinik',
        'update': 'masterData.change_poliklinik',
        'delete': 'masterData.delete_poliklinik',
    }

class BangsalCrud(BaseCrudBuilder):
    model = Bangsal
    tables2_css_class = "table table-bordered table-condensed"
    login_required = True
    permission_required = True
    search_fields = ['kode','name']
    tables2_fields = ('kode','name',)
    custom_postfix_url = 'master-data-bangsal'
    permissions = {
        'list'  : 'masterData.view_bangsal',
        'create': 'masterData.add_bangsal',
        'detail': 'masterData.view_bangsal',
        'update': 'masterData.change_bangsal',
        'delete': 'masterData.delete_bangsal',
    }

class kategori_perawatanCrud(BaseCrudBuilder):
    model = kategori_perawatan
    tables2_css_class = "table table-bordered table-condensed"
    login_required = True
    permission_required = True
    search_fields = ['kode','name']
    tables2_fields = ('kode','name',)
    custom_postfix_url = 'master-data-kategori-perawatan'
    permissions = {
        'list'  : 'masterData.view_kategori_perawatan',
        'create': 'masterData.add_kategori_perawatan',
        'detail': 'masterData.view_kategori_perawatan',
        'update': 'masterData.change_kategori_perawatan',
        'delete': 'masterData.delete_kategori_perawatan',
    }

class perawatan_rawat_jalanCrud(BaseCrudBuilder):
    model = perawatan_rawat_jalan
    tables2_css_class = "table table-bordered table-condensed"
    login_required = True
    permission_required = True
    search_fields = ['kode','nama_perawatan']
    tables2_fields = ('kode','nama_perawatan','kategori','status',)
    custom_postfix_url = 'master-data-perawatan-rawat-jalan'
    permissions = {
        'list'  : 'masterData.view_perawatan_rawat_jalan',
        'create': 'masterData.add_perawatan_rawat_jalan',
        'detail': 'masterData.view_perawatan_rawat_jalan',
        'update': 'masterData.change_perawatan_rawat_jalan',
        'delete': 'masterData.delete_perawatan_rawat_jalan',
    }
