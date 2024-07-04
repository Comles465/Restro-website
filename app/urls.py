from django.urls import path
from .views import *
urlpatterns = [
    path("",home,name="home"),
    path("aboutus/",aboutus,name="aboutus"),
    path("contactus/",contactus,name="contactus"),
    path("ourmenu/",ourmenu,name="ourmenu"),
    path("ourservices/",ourservices,name="ourservices"),
    path("allergyadvice/",allergyadvice,name="allergyadvice"),
    path("footer/",footer,name="footer"),
    path("buff/",buff,name="buff"),
    path("chicken/",chicken,name="chicken"),
    path("veg/",veg,name="veg"),
]
