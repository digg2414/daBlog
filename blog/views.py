from django.shortcuts import render
from blog.models import Post
from django.http import Http404
from django.shortcuts import get_object_or_404, render

# Create your views here.

"""
    Get the post if it of the Post class,
    matching id, or has a status of published.
"""
def post_detail(request, id):
    post = get_object_or_404(
        Post,
        id=id,
        status=Post.Status.PUBLISHED
    )
    return render(
        request,
        'blog/post_detail.html',
        {'post': post}
    )

def post_list(request): 
    posts = Post.published.all()
    return render(
        request,
        'blog/post_list.html',
        {'posts:': posts}
    )