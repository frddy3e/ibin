from . import views
from django.conf.urls import url

urlpatterns = [
        url(r'^estados_waste/$', views.estados_wasteView, name='estados_waste'),
		url(r'^inicio_waste/$', views.inicio_wasteView, name='inicio_waste'),
        url(r'^historico_waste/$', views.historico_wasteView, name='historico_waste'),
        url(r'^actualizar_waste/$', views.actualizar_wasteView, name='actualizar_waste'),
        ]