from django.conf.urls import url
from . import views
from django.views.generic import ListView, DetailView
from portal.models import Post

urlpatterns = [
	url(r'^$',views.index, name = 'index'),
	url(r'^login/$',views.login, name='login'),
	url(r'^blog/$', ListView.as_view(queryset=Post.objects.all().order_by("-date"), template_name="portal/blog.html"), name ='blog')
]