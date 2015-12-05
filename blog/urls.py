from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^show_write_form/$', views.show_write_form),
    url(r'^post_list/$', views.post_list),
    url(r'^DoWriteBoard/$', views.DoWriteBoard),
    url(r'^showpage/$', views.showpage),
    url(r'^search/$', views.search),
]
