from django.urls import path
from . import views as core_views

urlpatterns = [

    path('',core_views.home, name="home"),
    path('search_post',core_views.search_post, name="search_post"),


]

