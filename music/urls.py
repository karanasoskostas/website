from django.conf.urls import url
from . import views

app_name="music"

urlpatterns = [
    # /music/
    url(r'^$', views.index, name='index'),

    # /music/10/
    url(r'^(?P<album_id>[0-9]+)$', views.detail, name="detail"),

    # /music/10/
   # url(r'^(?P<album_id>[0-9]+)/(?P<album_id2>[0-9]+)$', views.detail2, name="detail2"),

]
