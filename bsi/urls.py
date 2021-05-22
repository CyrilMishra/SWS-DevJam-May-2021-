import community
from django.urls import path , include
from . import views
from community.views import search
urlpatterns = [

	path("bsihome",views.bsihome,name="bsihome"),
	path("sell",views.sell,name="sell"),
	path("buy",views.buy,name="buy"),
	path("sellpost",views.sellpost,name="sellpost"),
	path("useradds",views.useradds,name="useradds"),
	path("alladds",views.alladds,name="alladds"),
	path('sellupdate/<str:pk>/',views.sellupdate,name="sellupdate"),
	path("search",search,name="search"),
	path("selldelete/<str:pk>/", views.selldelete, name="selldelete"),
]