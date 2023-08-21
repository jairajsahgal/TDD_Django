from django.shortcuts import render
from posts.models import Post
# Create your views here.
def index(request):
    posts = Post.objects.all().order_by("-created_at")
    return render(request,"posts/index.html",context={'posts':posts})