from django.urls import path , include
from . import views

urlpatterns = [

	path("lfihome",views.lfihome,name="home"),
	path("lostreport",views.lostreport,name="lostreport"),
	path("foundreport",views.foundreport,name="foundreport"),
	path("lostentryadded",views.lostentryadded,name="lostentryadded"),
	path("founditemadded",views.founditemadded,name="founditemadded"),
	path("matchingitems",views.matchingitems,name="matchingitems"),
	path("userfoundentries",views.userfoundentries,name="userfoundentries"),
	path("userslostentries",views.userslostentries,name="userslostentries"),
]