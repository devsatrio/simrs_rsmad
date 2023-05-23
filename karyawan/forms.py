
from django import forms
from .models import Karyawan

class KaryawanForm(forms.ModelForm):
 
    class Meta:
        # specify model to be used
        model = Karyawan
 
        # specify fields to be used
        fields = [
            "nama",
            "nama_lengkap",
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