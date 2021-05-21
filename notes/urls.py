from django.conf.urls import url
from django.urls import path
from notes import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    url(r'^$', views.home, name='home_notes'),
    url(r'^course/(?P<pk>\d+)/$', views.course_file, name='course_file'),
    url(r'^course/(?P<pk>\d+)/view/$', views.view_files, name='view_files'),
    url(r'^course/(?P<pk>\d+)/upload/$', views.upload_file, name='upload_file'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


