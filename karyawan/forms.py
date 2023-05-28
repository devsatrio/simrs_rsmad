
from django import forms
from .models import Karyawan,BerkasKaryawan

#========================================================================================================================
class KaryawanForm(forms.ModelForm):
    class Meta:
        # specify model to be used
        model = Karyawan
 
        # specify fields to be used
        fields = [
            "nik",
            "nama",
            "nama_lengkap",
            "no_telfon",
            "no_karyawan_tetap",
            "tempat_lahir",
            "tgl_lahir",
            "no_str",
            "tgl_berlaku_str",
            "no_sip",
            "tgl_berlaku_sip",
            "user",
            "status_karyawan",
            "agama",
            "jenis_kelamin",
            "golongan_darah",
            "status_nikah",
            "golongan_karyawan",
            "jabatan_karyawan",
            "unit",
        ]
        widgets = {
            'tgl_lahir': forms.DateInput(attrs={'type': 'date'}),
            'tgl_berlaku_str': forms.DateInput(attrs={'type': 'date'}),
            'tgl_berlaku_sip': forms.DateInput(attrs={'type': 'date'})
        }

#========================================================================================================================
class BerkasSayaForm(forms.ModelForm):
 
    class Meta:
        # specify model to be used
        model = BerkasKaryawan
 
        # specify fields to be used
        fields = [
            "nama_berkas",
            "kategori",
            "berkas",
        ]

#========================================================================================================================
class BerkasKaryawanForm(forms.ModelForm):
 
    class Meta:
        # specify model to be used
        model = BerkasKaryawan
 
        # specify fields to be used
        fields = [
            "karyawan",
            "nama_berkas",
            "kategori",
            "berkas",
            "status_berkas",
            "keterangan_verifikator",
        ]