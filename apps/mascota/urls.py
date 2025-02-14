from django.conf.urls import url
from django.views.generic import detail
from django.conf import settings
from django.conf.urls.static import static

from .views import index, mascota_view, mascota_list, mascota_edit, mascota_delete, MascotaList, MascotaCreateView, MascotaUpdateView, MascotaDeleteView

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^class/nuevo$', MascotaCreateView.as_view(), name='class_mascota_crear'),
    url(r'^function/nuevo$', mascota_view, name='function_mascota_crear'),
    url(r'^class/listar$', MascotaList.as_view()  , name='class_mascota_listar'),
    url(r'^function/listar$', mascota_list, name='function_mascota_listar'),
    url(r'^class/editar/(?P<pk>\d+)/', MascotaUpdateView.as_view(), name='class_mascota_editar'),
    url(r'^function/editar/(?P<id_mascota>\d+)/', mascota_edit, name='function_mascota_editar'),
    url(r'^class/eliminar/(?P<pk>\d+)/', MascotaDeleteView.as_view(), name='class_mascota_eliminar'),
    url(r'^function/eliminar/(?P<id_mascota>\d+)/', mascota_delete, name='function_mascota_eliminar'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)