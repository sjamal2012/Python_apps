from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^log_reg$', views.index),
    url(r'^log_reg/register$', views.register),
    url(r'^log_reg/login$', views.login),
    url(r'^log_reg/logged_in$', views.logged_in)
]
