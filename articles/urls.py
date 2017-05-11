from django.conf.urls import url
from articles import views

app_name='articles'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^article/(?P<id_article>\d+)$', views.article, name="article"),
    url(r'^crear_article/$', views.crear_article, name="crear_article"),
    url(r'(?P<id_article>\d+)/eliminar_article/$', views.eliminar_article, name="eliminar_article"),
    url(r'^cercador/$', views.cercador, name="cercador"),
]