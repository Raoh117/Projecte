from django.conf.urls import url
from usuaris import views

app_name='usuaris'

urlpatterns = [
    url(r'^login/$', views.login, name='login'),
    url(r'^crear/$', views.crear_usuari,name="crear_usuari"),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^menu/$', views.menu_usuari,name="menu_usuari"),
]