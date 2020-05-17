from django.shortcuts import render,get_object_or_404
from .models import Post,Category
# Create your views here.
def posts(request):
    posts = Post.objects.all()
    category = Category.objects.all()
    print(category.count())
    return render(request,"blog/posts.html",{'posts':posts,'categories':category})

def category(request,category_id):
    category = get_object_or_404(Category,id=category_id)
    categories = Category.objects.all()
    #posts = Post.objects.filter(categories=category)
    return render(request,"blog/category.html",{'category':category,'categories':categories})

