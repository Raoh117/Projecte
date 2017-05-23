from django.conf.urls import url
from articles import views

app_name='articles'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^search/$', views.search, name="search"),
    url(r'^consoles', views.consoles, name='consoles'),
    url(r'^accesoris', views.accesoris, name='accesoris'),
    url(r'^videojocs', views.videojocs, name='videojocs'),
    url(r'^article/(?P<id_article>\d+)$', views.article, name="article"),
    url(r'^crear_article/$', views.crear_article, name="crear_article"),
    url(r'(?P<id_article>\d+)/eliminar_article/$', views.eliminar_article, name="eliminar_article"),
    url(r'(?P<id_article>\d+)/editar_article/$', views.editar_article, name="editar_article"),
    url(r'^fer_backups/$', views.fer_backups, name='fer_backups'),
]