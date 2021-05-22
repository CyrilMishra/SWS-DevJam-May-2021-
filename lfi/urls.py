from django.urls import path , include
from . import views

urlpatterns = [

	path("lfihome",views.lfihome,name="lfihome"),
	path("lostreport",views.lostreport,name="lostreport"),
	path("foundreport",views.foundreport,name="foundreport"),
	path("LFI/lostentryadded",views.lostentryadded,name="lostentryadded"),
	path("founditemadded",views.founditemadded,name="founditemadded"),
	path("matchingitems",views.matchingitems,name="matchingitems"),
	path("userfoundentries",views.userfoundentries,name="userfoundentries"),
	path("userslostentries",views.userslostentries,name="userslostentries"),

	path("foundreportdelete/<str:pk>/", views.foundreportdelete, name="foundreportdelete"),
	path("lostreportdelete/<str:pk>/", views.lostreportdelete, name="lostreportdelete"),

	path("foundreportupdate/<str:pk>/", views.foundreportupdate, name="foundreportupdate"),
	path("lostreportupdate/<str:pk>/", views.lostreportupdate, name="lostreportupdate"),

]