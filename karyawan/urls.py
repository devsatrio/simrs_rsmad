from django.urls import path
from . import views

app_name='karyawan'

urlpatterns = [
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
]
