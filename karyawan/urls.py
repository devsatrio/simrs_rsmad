from django.urls import path
from . import views

app_name='karyawan'

urlpatterns = [
	path('index',views.index,name='index'),
	path('create',views.create,name='create'),
	path('edit/<int:id>',views.edit,name='edit'),
	path('show/<int:id>',views.show,name='show'),
	path('destroy/<int:id>',views.destroy,name='destroy'),
]
