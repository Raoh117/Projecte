from django.conf.urls import url
from usuaris import views

app_name='usuaris'

urlpatterns = [
    url(r'^login/$', views.login, name='login'),
    url(r'^crear/$', views.crear_usuari,name="crear_usuari"),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^menu/$', views.menu_usuari,name="menu_usuari"),
    url(r'(?P<id_article>\d+)/afegir_al_carritu/$', views.afegir_al_carritu, name="afegir_al_carritu"),
    url(r'(?P<id_comanda>\d+)/eliminar_comanda/$', views.eliminar_comanda, name="eliminar_comanda"),
]