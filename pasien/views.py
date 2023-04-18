from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from masterWilayah.models import propinsi, kota, kecamatan, kelurahan

# Create your views here.
@login_required
def propinsi_list(request, negara_id):
    propinsi_data = propinsi.objects.filter(negara=negara_id)
    return JsonResponse({'data': [{'id': k.id, 'name': k.name} for k in propinsi_data]})

@login_required
def kota_list(request, propinsi_id):
    kota_data = kota.objects.filter(propinsi=propinsi_id)
    return JsonResponse({'data': [{'id': k.id, 'name': k.name} for k in kota_data]})

@login_required
def kecamatan_list(request, kota_id):
    kecamatan_data = kecamatan.objects.filter(kota=kota_id)
    return JsonResponse({'data': [{'id': k.id, 'name': k.name} for k in kecamatan_data]})

@login_required
def kelurahan_list(request, kecamatan_id):
    kelurahan_data = kelurahan.objects.filter(kecamatan=kecamatan_id)
    return JsonResponse({'data': [{'id': k.id, 'name': k.name} for k in kelurahan_data]})