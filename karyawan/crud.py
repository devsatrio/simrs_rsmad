from crudbuilder.abstract import BaseCrudBuilder
from .models import StatusKaryawan

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