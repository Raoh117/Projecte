from django.conf.urls import url
from usuaris import views
from django.conf.urls import url, include

app_name='usuaris'

urlpatterns = [
    url(r'^login/$', views.login, name='login'),
    url(r'^crear/$', views.crear_usuari,name="crear_usuari"),
    url(r'^crearA/$', views.crear_admin,name="crear_admin"),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^modificar/$', views.modificar_perfil,name="modificar_perfil"),
    url(r'^menu/$', views.menu_usuari,name="menu_usuari"),
    url(r'(?P<id_article>\d+)/afegir_al_carritu/$', views.afegir_al_carritu, name="afegir_al_carritu"),
    url(r'(?P<id_comanda>\d+)/eliminar_comanda/$', views.eliminar_comanda, name="eliminar_comanda"),
    url(r'(?P<id_carritu>\d+)/paypal/$', views.view_that_asks_for_money,name="view_that_asks_for_money"),
    url(r'(?P<id_carritu>\d+)/pagat/$', views.pagat,name="pagat"),
]

