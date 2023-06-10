from django_filters import FilterSet
from .models import Karyawan,BerkasKaryawan,KarirKaryawan,RiwayatPendidikanKaryawan,PelatihanKaryawan

# =========================================================================================================
class PelatihanKaryawanFilter(FilterSet):
    class Meta:
        model = PelatihanKaryawan
        fields = {
            "karyawan": ["exact"],
            "nama_pelatihan": ["exact"],
            "tahun_kegiatan": ["exact"],
            }
        
# =========================================================================================================
class RiwayatPendidikanKaryawanFilter(FilterSet):
    class Meta:
        model = RiwayatPendidikanKaryawan
        fields = {
            "karyawan": ["exact"],
            "strata_pendidikan": ["exact"],
            "nama_sekolah": ["contains"],
            "tahun_lulus": ["exact"],
            }
        
# =========================================================================================================
class KarirKaryawanFilter(FilterSet):
    class Meta:
        model = KarirKaryawan
        fields = {
            "karyawan": ["exact"],
            "unit": ["exact"],
            "jabatan": ["exact"],
            "tahun_menjabat": ["exact"],
            }

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