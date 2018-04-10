from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^surveys/process$', views.process),
    url(r'^survey$', views.result)     # This line has changed!
]
