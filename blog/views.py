from django.shortcuts import render, get_object_or_404
from .models import BlogPost
from datetime import datetime

def home(request):
    query = request.GET.get('q')
    if query:
        posts = BlogPost.objects.filter(title__icontains=query)
    else:
        posts = BlogPost.objects.all()
    return render(request, 'blog/home.html', {
        'posts': posts,
        'year': datetime.now().year
    })

def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    return render(request, 'blog/blog_detail.html', {
        'post': post,
        'year': datetime.now().year
    })
