
from django.urls import path
from .views import listfunc,detailfunc,goodfunc,readfunc,deletefunc,signupfunc,loginfunc,logoutfunc,createfunc,updatefunc



urlpatterns = [

    path("",signupfunc,name="signup1"),
    path("list/",listfunc,name="list"),
    path("detail/<int:pk>",detailfunc,name="detail"),
    path("update/<int:pk>",updatefunc,name="update"),
    path("delete/<int:pk>",deletefunc,name="delete"),
    path("create/",createfunc,name="create"),
    path("good/<int:pk>",goodfunc,name="good"),
    path("read/<int:pk>",readfunc,name="read"),
    path("login/",loginfunc,name="login"),
    path("logout/",logoutfunc,name="logout"),
    path("signup/",signupfunc,name="signup"),

    ]
