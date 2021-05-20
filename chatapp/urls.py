from django.urls import path, include
from chatapp import views

urlpatterns = [
    path("chatapp", views.chatapp, name='chatapp'),
    path("conversation", views.converstion, name="conversation"),
]
