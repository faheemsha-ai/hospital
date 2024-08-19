from django.urls import path
from . import views

urlpatterns = [
    path("",views.index , name="index"),
    path("404",views.error,name="404"),
    path("blog",views.blog,name="blog"),
    path("contact",views.contact,name="contact"),
    path("portfolio",views.port,name="port")
]