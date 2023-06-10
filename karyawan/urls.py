from django.urls import path
from . import views

app_name='karyawan'

urlpatterns = [
    path('cari-berkas/<int:karyawan_id>', views.berkas_list, name = 'berkas_list'),
    
    # karyawan
	path('index',views.index,name='index'),
	path('create',views.create,name='create'),
	path('edit/<int:id>',views.edit,name='edit'),
	path('show/<int:id>',views.show,name='show'),
	path('destroy/<int:id>',views.destroy,name='destroy'),
    
	# berkas saya
	path('berkas-saya',views.indexberkassaya,name='berkas-saya-index'),
    path('create-berkas-saya',views.createberkassaya,name='berkas-saya-create'),
	path('show-berkas-saya/<int:id>',views.showberkassaya,name='berkas-saya-show'),
	path('edit-berkas-saya/<int:id>',views.editberkassaya,name='berkas-saya-edit'),
	path('destroy-berkas-saya/<int:id>',views.destroyberkassaya,name='berkas-saya-destroy'),
    
	# berkas karyawan
	path('berkas-karyawan',views.indexberkaskaryawan,name='berkas-karyawan-index'),
	path('create-berkas-karyawan',views.createberkaskaryawan,name='berkas-karyawan-create'),
	path('show-berkas-karyawan/<int:id>',views.showberkaskaryawan,name='berkas-karyawan-show'),
	path('edit-berkas-karyawan/<int:id>',views.editberkaskaryawan,name='berkas-karyawan-edit'),
	path('destroy-berkas-karyawan/<int:id>',views.destroyberkaskaryawan,name='berkas-karyawan-destroy'),
	
	# Karir karyawan
	path('karir-karyawan',views.indexkarirkaryawan,name='karir-karyawan-index'),
	path('create-karir-karyawan',views.createkarirkaryawan,name='karir-karyawan-create'),
	path('show-karir-karyawan/<int:id>',views.showkarirkaryawan,name='karir-karyawan-show'),
	path('edit-karir-karyawan/<int:id>',views.editkarirkaryawan,name='karir-karyawan-edit'),
	path('destroy-karir-karyawan/<int:id>',views.destroykarirkaryawan,name='karir-karyawan-destroy'),
    
	# Riwayat Pendidikan karyawan
	path('riwayat-pendidikan-karyawan',views.indexriwayatpendidikankaryawan,name='riwayat-pendidikan-karyawan-index'),
	path('create-riwayat-pendidikan-karyawan',views.createriwayatpendidikankaryawan,name='riwayat-pendidikan-karyawan-create'),
	path('show-riwayat-pendidikan-karyawan/<int:id>',views.showriwayatpendidikankaryawan,name='riwayat-pendidikan-karyawan-show'),
	path('edit-riwayat-pendidikan-karyawan/<int:id>',views.editriwayatpendidikankaryawan,name='riwayat-pendidikan-karyawan-edit'),
	path('destroy-riwayat-pendidikan-karyawan/<int:id>',views.destroyriwayatpendidikankaryawan,name='riwayat-pendidikan-karyawan-destroy'),
	
	# Pelatihan karyawan
	path('pelatihan-karyawan',views.indexpelatihankaryawan,name='pelatihan-karyawan-index'),
	path('create-pelatihan-karyawan',views.createpelatihankaryawan,name='pelatihan-karyawan-create'),
	path('show-pelatihan-karyawan/<int:id>',views.showpelatihankaryawan,name='pelatihan-karyawan-show'),
	path('edit-pelatihan-karyawan/<int:id>',views.editpelatihankaryawan,name='pelatihan-karyawan-edit'),
	path('destroy-pelatihan-karyawan/<int:id>',views.destroypelatihankaryawan,name='pelatihan-karyawan-destroy'),
]
