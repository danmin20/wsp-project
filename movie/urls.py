from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^$', views.movie_list, name='movie_list'),
  url(r'^post/(?P<pk>\d+)/$', views.post_detail, name="post_detail"),
  url(r'^post/new/(?P<title>[\w\-]+)/$', views.post_new, name="post_new"),
  url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name="post_edit"),
  url(r'^posts/(?P<title>[\w\-]+)/$', views.post_list, name="post_list"),
  url(r'^signup/$', views.signup, name="signup"),
  url(r'^logout/$', views.logout, name="logout"),
]