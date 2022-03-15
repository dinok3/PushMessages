from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("delete/<int:pk>/",views.deleteNote,name="delete"),
    path("update/<int:pk>/",views.updateNote,name="update"),
    path("send/",views.sendMail,name="send"),
   
]

