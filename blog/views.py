from django.shortcuts import render
from django.utils import timezone
from .models import Post

def members_list(request):
    posts = Post.objects.order_by('created_date').order_by('published_date')
    return render(request, 'blog/members_list.html', {'posts': posts})