from django.urls import path , include
from . import views

urlpatterns = [

	path("bsihome",views.bsihome,name="home"),
	path("sell",views.sell,name="sell"),
	path("buy",views.buy,name="buy"),
	path("sellpost",views.sellpost,name="sellpost"),
	path("useradds",views.useradds,name="useradds"),
	path("alladds",views.alladds,name="alladds"),
	path("updatePost",views.updatePost,name="updatePost"),
	path("deletePost",views.deletePost,name="deletePost"),
]