from django.conf.urls import include, url

from blog import views

urlpatterns = [
	url(r'^$',views.index, name='index'),
    url(r'^column/(?P<column_slug>[^/]+)$',views.column_detail, name='column_detail'),
    url(r'^column/$',views.columns, name='columns'),
    url(r'^article/(?P<pk>\d+)$',views.article, name='article'),
]