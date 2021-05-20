from django.contrib import admin
from django.urls import path, include
from community import views

urlpatterns = [
    path("community", views.community, name='community'),
    path("profile", views.profile, name='profile'),
    path("communityanswer", views.communityanswer, name='communityanswer'),
    path("logout",views.logout,name="logout")
]
