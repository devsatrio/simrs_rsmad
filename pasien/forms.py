from django import forms
from .models import pasien
from masterWilayah.models import negara, propinsi, kota, kecamatan, kelurahan


class pasienForm(forms.ModelForm):
    class Meta:
        model = pasien
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(pasienForm, self).__init__(*args, **kwargs)

        try:
            self.initial['negara'] = kwargs['instance'].negara.id
        except:
            pass
        negara_list = [('', '---------')] + [(i.id, i.name) for i in negara.objects.all()]

        try:
            self.initial['propinsi'] = kwargs['instance'].propinsi.id
            propinsi_init_form = [(i.id, i.name) for i in propinsi.objects.filter(
                propinsi=kwargs['instance'].propinsi
            )]
        except:
            propinsi_init_form = [('', '---------')] + [(i.id, i.name) for i in propinsi.objects.all()]
        
        try:
            self.initial['kota'] = kwargs['instance'].kota.id
            kota_init_form = [(i.id, i.name) for i in kota.objects.filter(
                kota=kwargs['instance'].kota
            )]
        except:
            kota_init_form = [('', '---------')] + [(i.id, i.name) for i in kota.objects.all()]

        try:
            self.initial['kecamatan'] = kwargs['instance'].kecamatan.id
            kecamatan_init_form = [(i.id, i.name) for i in kecamatan.objects.filter(
                kecamatan=kwargs['instance'].kecamatan
            )]
        except:
            kecamatan_init_form = [('', '---------')] + [(i.id, i.name) for i in kecamatan.objects.all()]

        try:
            self.initial['kelurahan'] = kwargs['instance'].kelurahan.id
            kelurahan_init_form = [(i.id, i.name) for i in kelurahan.objects.filter(
                kelurahan=kwargs['instance'].kelurahan
            )]
        except:
            kelurahan_init_form = [('', '---------')] + [(i.id, i.name) for i in kelurahan.objects.all()]

        # Override the form, add onchange attribute to call the ajax function
        self.fields['negara'].widget = forms.Select(
            attrs={
                'id': 'id_negara',
                'onchange': 'getPropinsi(this.value)',
                'style': 'width:200px'
            },
            choices=negara_list,
        )
        
        self.fields['propinsi'].widget = forms.Select(
            attrs={
                'id': 'id_propinsi',
                'onchange': 'getKota(this.value)',
                'style': 'width:200px'
            },
            choices=propinsi_init_form
        )
        
        self.fields['kota'].widget = forms.Select(
            attrs={
                'id': 'id_kota',
                'onchange': 'getKecamatan(this.value)',
                'style': 'width:200px'
            },
            choices=kota_init_form
        )
        
        self.fields['kecamatan'].widget = forms.Select(
            attrs={
                'id': 'id_kecamatan',
                'onchange': 'getKelurahan(this.value)',
                'style': 'width:200px'
            },
            choices=kecamatan_init_form
        )
        
        self.fields['kelurahan'].widget = forms.Select(
            attrs={
                'id': 'id_kelurahan',
                'style': 'width:200px'
            },
            choices=kelurahan_init_form
        )