from django.urls import path,include
from myproject import views

urlpatterns=[
    path("home/",views.home,name="home"),
    path("main/",views.main,name="main"),
    path("group/", views.group, name="group"),
    path("indian/",views.indian,name="indian"),
]