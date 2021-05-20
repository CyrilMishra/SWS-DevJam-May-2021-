from django.urls import path , include
from . import views

urlpatterns = [

	path("signup",views.signup, name="signup"),
	path("login",views.login, name="login"),
	path("home",views.home, name="home"),
	path('',views.user_registration),
	#path("update_profile/<str:pk>/",views.update_profile,name="update_profile")

	#BSI URLS STARTS

	# path('BSI/<str:pk>',include('bsi.urls')),
]