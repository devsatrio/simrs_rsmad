
from django import forms
from .models import Karyawan,BerkasKaryawan,RiwayatPendidikanKaryawan

class RiwayatPedidikanKaryawanAdminForm(forms.ModelForm):
    class Meta:
        model = RiwayatPendidikanKaryawan
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super(RiwayatPedidikanKaryawanAdminForm, self).__init__(*args, **kwargs)

        try:
            self.initial['karyawan'] = kwargs['instance'].karyawan.id
        except:
            pass
        karyawan_list = [('', '---------')] + [(i.id, i.nama) for i in Karyawan.objects.all()]

        try:
            self.initial['berkas'] = kwargs['instance'].BerkasKaryawan.id
            berkas_init_form = [(i.id, i.nama_berkas) for i in BerkasKaryawan.objects.filter(karyawan=kwargs['instance'].karyawan).filter(status_berkas='Berkas Diterima')]
        except:
            try:
                berkas_init_form = [('', '---------'),] +[(i.id, i.nama_berkas) for i in BerkasKaryawan.objects.filter(karyawan=kwargs['instance'].karyawan).filter(status_berkas='Berkas Diterima')]
            except:
                berkas_init_form = [('', '---------'),]
        
        # Override the form, add onchange attribute to call the ajax function
        self.fields['karyawan'].widget = forms.Select(
            attrs={
                'id': 'karyawan',
                'onchange': 'getBerkasKaryawan(this.value)',
                'style': 'width:200px'
            },
            choices=karyawan_list,
        )

        self.fields['berkas'].widget = forms.Select(
            attrs={
                'id': 'berkas_karyawan',
                'style': 'width:200px'
            },
            choices=berkas_init_form,
        )


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