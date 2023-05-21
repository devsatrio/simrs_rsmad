import django_tables2 as tables
from .models import Karyawan
from django_tables2.utils import A

class KaryawanTable(tables.Table):
    aksi = tables.LinkColumn('karyawan:show', text='Show', args=[A('pk')])

    class Meta:
        model=Karyawan