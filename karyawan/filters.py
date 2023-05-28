from django_filters import FilterSet
from .models import Karyawan,BerkasKaryawan

# =========================================================================================================
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

# =========================================================================================================
class BerkasSayaFilter(FilterSet):
    class Meta:
        model = BerkasKaryawan
        fields = {
            "nama_berkas": ["contains"],
            "kategori": ["exact"],
            "verifikator": ["exact"],
            }

# =========================================================================================================
class BerkasKaryawanFilter(FilterSet):
    class Meta:
        model = BerkasKaryawan
        fields = {
            "karyawan": ["exact"],
            "nama_berkas": ["contains"],
            "kategori": ["exact"],
            "verifikator": ["exact"],
            }