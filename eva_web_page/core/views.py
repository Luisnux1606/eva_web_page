from django.shortcuts import render,HttpResponse
from blog.models import Post

# Create your views here.

def home(request):
    return render(request,"core/home.html") 

def search_post(request):
    if request.method == 'POST':      
        post_to_search =  request.POST.getlist('search_post')      
        try:
            status = Post.objects.filter(content__icontains=post_to_search[0])
            
            #Add_prod class contains a column called 'bookname'
        except Post.DoesNotExist:
            status = None
            return render(request,"blog/posts.html",{"posts":status})
        else:
            return render(request,"blog/posts.html",{"posts":status})
