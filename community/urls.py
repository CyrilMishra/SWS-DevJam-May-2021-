from django.contrib import admin
from django.urls import path, include
from community import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("community", views.community, name='community'),
    path("profile", views.profile, name='profile'),
    path("communityanswer", views.communityanswer, name='communityanswer'),
    path("ManagePost",views.ManagePost,name="ManagePost"),
    path("logout",views.logout,name="logout"),
    path("EditPost",views.EditPost,name="EditPost"),
    path("search",views.search,name="search")

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)