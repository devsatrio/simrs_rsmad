from django_filters import FilterSet
from .models import Karyawan

class KaryawanFilter(FilterSet):
    class Meta:
        model = Karyawan
        fields = {
            "nama": ["contains"], 
            "nama_lengkap": ["contains"],
            "status_karyawan": ["exact"],
            "agama": ["exact"],
            "jenis_kelamin": ["exact"],
            "status_nikah": ["exact"],
            }