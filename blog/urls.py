from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^accueil/?$', views.home, name='home'),
    url(r'^date/?$', views.date_actuelle, name='date'),
    url(r'^addition/(?P<nombre1>\d+)/(?P<nombre2>\d+)/?$', views.addition, name='addition'),
    url(r'^signup/?$', views.inscription_form, name='inscription_form'),
    url(r'^DoSignup/?$', views.inscription, name='inscription'),
    url(r'^article/(?P<id>\d*)/?$', views.article, name='article'),
]