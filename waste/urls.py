from . import views
from django.conf.urls import url

urlpatterns = [
        url(r'^estados_waste/$', views.estados_wasteView),
		url(r'^inicio_waste/$', views.inicio_wasteView),
        url(r'^historico_waste/$', views.historico_wasteView),
        url(r'^actualizar_waste/$', views.actualizar_wasteView),
        
        ]