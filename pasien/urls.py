from django.urls import path
from . import views

urlpatterns = [
    path('cari-propinsi/<int:negara_id>', views.propinsi_list, name = 'propinsi_list'),
    path('cari-kota/<int:propinsi_id>', views.kota_list, name = 'kota_list'),
    path('cari-kecamatan/<int:kota_id>', views.kecamatan_list, name = 'kecamatan_list'),
    path('cari-kelurahan/<int:kecamatan_id>', views.kelurahan_list, name = 'kelurahan_list')
]