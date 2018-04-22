from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),   # This line has changed! Notice that urlpatterns is a list, the comma is in
    url(r'^success$', views.success),
    url(r'^process$', views.process),
    url(r'^login$', views.login)
]                            # anticipation of all the routes that will be coming soon
