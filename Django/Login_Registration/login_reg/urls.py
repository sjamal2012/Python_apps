from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^login_reg$', views.index),
    url(r'^login_reg/register$', views.register),
    url(r'^login_reg/login$', views.login),
    url(r'^login_reg/logged_in$', views.logged_in)
]
