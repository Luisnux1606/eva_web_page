from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator
from .models import Post,Category
# Create your views here.
def posts(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 3)
    page = request.GET.get('page', 1)
    try:
        posts= paginator.page(page)
    except PageNotAnInteger:
        posts= paginator.page(1)
    except EmptyPage:
        posts= paginator.page(paginator.num_pages)

    return render(request,"blog/posts.html",{'posts':posts})

def post(request,post_id):
    post = get_object_or_404(Post,id=post_id)
    return render(request,"blog/standard-post.html",{'post':post})


def category(request,category_id):
    category = get_object_or_404(Category,id=category_id)
    return render(request,"blog/category.html",{'category':category})

