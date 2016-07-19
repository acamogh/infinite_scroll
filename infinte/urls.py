from django.conf.urls import url
from django.contrib import admin
from infinte import views

urlpatterns = [
    # url(r'^$', views.home, name='home'),
    # url(r'^', views.ThemeList.as_view()),
    url(r'^theme/$', views.themes, name='home'),
    # url(r'^api/(?P<pk>[0-9]+)/$', views.PostDetail.as_view()),


]