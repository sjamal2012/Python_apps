from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^amadon$', views.index),
    url(r'^process/(?P<item_id>\d+)', views.process),
    url(r'^amadon/checkout$', views.checkout)
    # url(r'^survey$', views.result)     # This line has changed!
]
