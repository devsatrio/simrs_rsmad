from crudbuilder.abstract import BaseCrudBuilder
from .models import StatusKaryawan,GolonganKaryawan,JabatanKaryawan,KategoriBerkasKaryawan

class StatusKaryawanCrud(BaseCrudBuilder):
    model = StatusKaryawan
    tables2_css_class = "table table-bordered table-condensed"
    login_required = True
    permission_required = True
    search_fields = ['name']
    tables2_fields = ('name',)
    custom_postfix_url = 'status-karyawan'
    permissions = {
        'list'  : 'karyawan.view_statuskaryawan',
        'create': 'karyawan.add_statuskaryawan',
        'detail': 'karyawan.view_statuskaryawan',
        'update': 'karyawan.change_statuskaryawan',
        'delete': 'karyawan.delete_statuskaryawan',
    }

class GolonganKaryawannCrud(BaseCrudBuilder):
    model = GolonganKaryawan
    tables2_css_class = "table table-bordered table-condensed"
    login_required = True
    permission_required = True
    search_fields = ['nama','keterangan']
    tables2_fields = ('nama','keterangan')
    custom_postfix_url = 'golongan-karyawan'
    permissions = {
        'list'  : 'karyawan.view_golongankaryawan',
        'create': 'karyawan.add_golongankaryawan',
        'detail': 'karyawan.view_golongankaryawan',
        'update': 'karyawan.change_golongankaryawan',
        'delete': 'karyawan.delete_golongankaryawan',
    }


class JabatanKaryawanCrud(BaseCrudBuilder):
    model = JabatanKaryawan
    tables2_css_class = "table table-bordered table-condensed"
    login_required = True
    permission_required = True
    search_fields = ['nama','keterangan']
    tables2_fields = ('nama','keterangan')
    custom_postfix_url = 'jabatan-karyawan'
    permissions = {
        'list'  : 'karyawan.view_jabatankaryawan',
        'create': 'karyawan.add_jabatankaryawan',
        'detail': 'karyawan.view_jabatankaryawan',
        'update': 'karyawan.change_jabatankaryawan',
        'delete': 'karyawan.delete_jabatankaryawan',
    }

class KategoriBerkasKaryawanCrud(BaseCrudBuilder):
    model = KategoriBerkasKaryawan
    tables2_css_class = "table table-bordered table-condensed"
    login_required = True
    permission_required = True
    search_fields = ['nama','keterangan']
    tables2_fields = ('nama','keterangan')
    custom_postfix_url = 'kategori-berkas-karyawan'
    permissions = {
        'list'  : 'karyawan.view_kategoriberkaskaryawan',
        'create': 'karyawan.add_kategoriberkaskaryawan',
        'detail': 'karyawan.view_kategoriberkaskaryawan',
        'update': 'karyawan.change_kategoriberkaskaryawan',
        'delete': 'karyawan.delete_kategoriberkaskaryawan',
    }