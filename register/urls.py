import community
from django.contrib import admin
from django.urls import path, include
from . import views
from notes.views import home
from community.views import search
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

                  path("signup", views.signup, name="signup"),
                  path("login", views.login, name="login"),
                  path("home", views.home, name="home"),
                  path('', views.user_registration),
                  path("notes", home, name="notes"),
                  path("search", search, name="search"),
                  # path("update_profile/<str:pk>/",views.update_profile,name="update_profile")

                  # BSI URLS STARTS

                  # path('BSI/<str:pk>',include('bsi.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
