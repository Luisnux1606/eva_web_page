from django.urls import path
from . import views as blog_views

urlpatterns = [

    path('',blog_views.posts, name="blog"),
    path('category/<int:category_id>/',blog_views.category, name="category"),
    path('post/<int:post_id>/',blog_views.post, name="post"),

]

