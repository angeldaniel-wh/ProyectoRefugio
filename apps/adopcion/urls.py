from django.conf.urls import url

from .views import index_adopcion, SolicitudList, SolicitudCreate, SolicitudUpdate, SolicitudDelete, solicitud_list, solicitud_create, solicitud_update, solicitud_delete

urlpatterns = [
    url(r'^index$', index_adopcion),  # Ensure index_adopcion is a valid view
    url(r'^class/solicitud/listar$', SolicitudList.as_view(), name='class_solicitud_listar'),
    url(r'^function/solicitud/listar$', solicitud_list, name='function_solicitud_listar'),
    url(r'^class/solicitud/nueva$', SolicitudCreate.as_view(), name='class_solicitud_crear'),
    url(r'^function/solicitud/nueva$', solicitud_create, name='function_solicitud_crear'),
    url(r'^class/solicitud/editar/(?P<pk>\d+)$', SolicitudUpdate.as_view(), name='class_solicitud_editar'),
    url(r'^function/solicitud/editar/(?P<pk>\d+)$', solicitud_update, name='function_solicitud_editar'),
    url(r'^class/solicitud/eliminar/(?P<pk>\d+)$', SolicitudDelete.as_view(), name='class_solicitud_eliminar'),
    url(r'^function/solicitud/eliminar/(?P<pk>\d+)$', solicitud_delete, name='function_solicitud_eliminar'),
]