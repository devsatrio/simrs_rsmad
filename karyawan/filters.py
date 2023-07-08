from django_filters import FilterSet
from .models import Karyawan,BerkasKaryawan,KarirKaryawan,RiwayatPendidikanKaryawan,PelatihanKaryawan

# =========================================================================================================
class PelatihanSayaFilter(FilterSet):
    class Meta:
        model = PelatihanKaryawan
        fields = {
            "nama_pelatihan": ["exact"],
            "tahun_kegiatan": ["exact"],
            }
        
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
class RiwayatPendidikanSayaFilter(FilterSet):
    class Meta:
        model = RiwayatPendidikanKaryawan
        fields = {
            "strata_pendidikan": ["exact"],
            "nama_sekolah": ["contains"],
            "tahun_lulus": ["exact"],
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
class KarirSayaFilter(FilterSet):
    class Meta:
        model = KarirKaryawan
        fields = {
            "unit": ["exact"],
            "jabatan": ["exact"],
            "tahun_menjabat": ["exact"],
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
            "kode": ["contains"],
            "nama": ["contains"], 
            "nama_lengkap": ["contains"],
            "nik": ["contains"],
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