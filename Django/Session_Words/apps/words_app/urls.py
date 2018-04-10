from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^session_words$', views.index),
    url(r'^add$', views.add),
    url(r'^clear$', views.clear)
    # url(r'^survey$', views.result)     # This line has changed!
]
