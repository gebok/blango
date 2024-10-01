from django.shortcuts import render
from django.utils import timezone
from blog.models import Post

def index(request):
    posts = Post.objects.filter(published_at__lte=timezone.now()).order_by('-published_at')
    return render(request, "blog/index.html", {"posts": posts})
