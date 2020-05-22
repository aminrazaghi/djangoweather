from django.urls import path
from . import views

urlpatterns = [
    #path('about.html', views.home, name="home" ),
    path('', views.home, name="home" ),
    path('about.html', views.about, name="about" ),

]