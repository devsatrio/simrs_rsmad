
from django import forms
from .models import Karyawan,BerkasKaryawan,RiwayatPendidikanKaryawan,KarirKaryawan,PelatihanKaryawan

#========================================================================================================================
class DataKaryawanSayaForm(forms.ModelForm):
    required_css_class = 'required'
    class Meta:
        # specify model to be used
        model = Karyawan
        # specify fields to be used
        fields = [
            "nama",
            "nama_lengkap",
            "no_telfon",
            "tempat_lahir",
            "tgl_lahir",
            "agama",
            "jenis_kelamin",
            "golongan_darah",
            "status_nikah",
            "foto",
        ]
        widgets = {
            'tgl_lahir': forms.DateInput(attrs={'type': 'date'}),
        }


#========================================================================================================================
class PelatihanSayaForm(forms.ModelForm):
    class Meta:
        model = PelatihanKaryawan
        fields = [
            "nama_pelatihan",
            "tanggal_pelatihan",
            "tahun_kegiatan",
            "tahun_expired",
            "berkas",
        ]
        widgets = {
            'tanggal_pelatihan': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self,user, *args, **kwargs):
        self.user=user
        super(PelatihanSayaForm, self).__init__(*args, **kwargs)

        try:
            berkas_init_form = [(i.id, i.nama_berkas) for i in BerkasKaryawan.objects.filter(karyawan=Karyawan.objects.get(user=user)).filter(status_berkas='Berkas Diterima')]
        except:
            pass
        berkas_init_form = [('', '---------'),] +[(i.id, i.nama_berkas) for i in BerkasKaryawan.objects.filter(karyawan=Karyawan.objects.get(user=user)).filter(status_berkas='Berkas Diterima')]
        
        
        # Override the form, add onchange attribute to call the ajax function
        self.fields['berkas'].widget = forms.Select(
            attrs={
                'id': 'berkas_karyawan',
            },
            choices=berkas_init_form,
        )

#========================================================================================================================
class PelatihanKaryawanForm(forms.ModelForm):
    class Meta:
        model = PelatihanKaryawan
        fields = '__all__'
        widgets = {
            'tanggal_pelatihan': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(PelatihanKaryawanForm, self).__init__(*args, **kwargs)

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
                'onchange': 'getBerkasKaryawanDua(this.value)',
            },
            choices=karyawan_list,
        )

        self.fields['berkas'].widget = forms.Select(
            attrs={
                'id': 'berkas_karyawan',
            },
            choices=berkas_init_form,
        )

#========================================================================================================================
class PelatihanKaryawanAdminForm(forms.ModelForm):
    class Meta:
        model = PelatihanKaryawan
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PelatihanKaryawanAdminForm, self).__init__(*args, **kwargs)

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
            },
            choices=karyawan_list,
        )

        self.fields['berkas'].widget = forms.Select(
            attrs={
                'id': 'berkas_karyawan',
            },
            choices=berkas_init_form,
        )

#========================================================================================================================
class KarirKaryawanAdminForm(forms.ModelForm):
    class Meta:
        model = KarirKaryawan
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(KarirKaryawanAdminForm, self).__init__(*args, **kwargs)

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
            },
            choices=karyawan_list,
        )

        self.fields['berkas'].widget = forms.Select(
            attrs={
                'id': 'berkas_karyawan',
            },
            choices=berkas_init_form,
        )
#========================================================================================================================
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
            },
            choices=karyawan_list,
        )

        self.fields['berkas'].widget = forms.Select(
            attrs={
                'id': 'berkas_karyawan',
            },
            choices=berkas_init_form,
        )

#========================================================================================================================
class KaryawanForm(forms.ModelForm):
    kode = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Minimal 8 karakter'}))
    required_css_class = 'required'
    class Meta:
        # specify model to be used
        model = Karyawan
        # specify fields to be used
        fields = [
            "kode",
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
            "foto",
        ]
        widgets = {
            'tgl_lahir': forms.DateInput(attrs={'type': 'date'}),
            'tgl_berlaku_str': forms.DateInput(attrs={'type': 'date'}),
            'tgl_berlaku_sip': forms.DateInput(attrs={'type': 'date'})
        }

#========================================================================================================================
class BerkasSayaForm(forms.ModelForm):
    required_css_class = 'required'
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
class RiwayatPendidikanSayaForm(forms.ModelForm):
    required_css_class = 'required'
    class Meta:
        # specify model to be used
        model = RiwayatPendidikanKaryawan
 
        # specify fields to be used
        fields = [
            "strata_pendidikan",
            "nama_sekolah",
            "tahun_lulus",
            "berkas",
        ]
    
    def __init__(self,user, *args, **kwargs):
        self.user=user
        super(RiwayatPendidikanSayaForm, self).__init__(*args, **kwargs)

        try:
            berkas_init_form = [(i.id, i.nama_berkas) for i in BerkasKaryawan.objects.filter(karyawan=Karyawan.objects.get(user=user)).filter(status_berkas='Berkas Diterima')]
        except:
            pass
        berkas_init_form = [('', '---------'),] +[(i.id, i.nama_berkas) for i in BerkasKaryawan.objects.filter(karyawan=Karyawan.objects.get(user=user)).filter(status_berkas='Berkas Diterima')]
           
        
        # Override the form, add onchange attribute to call the ajax function
        self.fields['berkas'].widget = forms.Select(
            attrs={
                'id': 'berkas_karyawan',
            },
            choices=berkas_init_form,
        )

#========================================================================================================================
class RiwayatPendidikanKaryawanForm(forms.ModelForm):
    required_css_class = 'required'
    class Meta:
        # specify model to be used
        model = RiwayatPendidikanKaryawan
 
        # specify fields to be used
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super(RiwayatPendidikanKaryawanForm, self).__init__(*args, **kwargs)

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
                'onchange': 'getBerkasKaryawanDua(this.value)',
            },
            choices=karyawan_list,
        )

        self.fields['berkas'].widget = forms.Select(
            attrs={
                'id': 'berkas_karyawan',
            },
            choices=berkas_init_form,
        )

#========================================================================================================================
class BerkasKaryawanForm(forms.ModelForm):
    required_css_class = 'required'
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
    
#========================================================================================================================
class KarirKaryawanForm(forms.ModelForm):
    required_css_class = 'required'
    class Meta:
        model = KarirKaryawan
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(KarirKaryawanForm, self).__init__(*args, **kwargs)

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
                'onchange': 'getBerkasKaryawanDua(this.value)',
            },
            choices=karyawan_list,
        )

        self.fields['berkas'].widget = forms.Select(
            attrs={
                'id': 'berkas_karyawan',
            },
            choices=berkas_init_form,
        )
        
#========================================================================================================================
class KarirSayaForm(forms.ModelForm):
    required_css_class = 'required'
    class Meta:
        model = KarirKaryawan
        # specify fields to be used
        fields = [
            "unit",
            "jabatan",
            "tahun_menjabat",
            "tahun_berhenti_menjabat",
            "berkas",
        ]

    def __init__(self,user, *args, **kwargs):
        self.user=user
        super(KarirSayaForm, self).__init__(*args, **kwargs)

        try:
            self.initial['berkas'] = kwargs['instance'].BerkasKaryawan.id
            berkas_init_form = [(i.id, i.nama_berkas) for i in BerkasKaryawan.objects.filter(karyawan=Karyawan.objects.get(user=user)).filter(status_berkas='Berkas Diterima')]
        except:
            pass
        berkas_init_form = [('', '---------'),] +[(i.id, i.nama_berkas) for i in BerkasKaryawan.objects.filter(karyawan=Karyawan.objects.get(user=user)).filter(status_berkas='Berkas Diterima')]
        
        # Override the form, add onchange attribute to call the ajax function
        self.fields['berkas'].widget = forms.Select(
            attrs={
                'id': 'berkas_karyawan',
            },
            choices=berkas_init_form,
        )