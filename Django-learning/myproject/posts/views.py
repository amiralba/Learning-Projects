from django.shortcuts import render
from .models import Post
from django.http import HttpResponse

def posts_list(request):
    posts = Post.objects.all().order_by('-date')
    return render(request, 'posts/posts_list.html', { 'posts': posts})


def post_page(request, slug):
    return HttpResponse(slug)   