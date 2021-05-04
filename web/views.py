from django.shortcuts import render, get_object_or_404
from django.templatetags.static import static
from django.utils import timezone
from .models import Post, PostImages

# Create your views here.


def index(request):
    logo_gray = static('images/logo_gray.png')
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by("-published_date")
    context = {
        'title': 'Home',
        'logo_gray': logo_gray,
        'posts': posts,
    }
    return render(request, 'web/index.html', context)


def detail_view(request, id):
    post = get_object_or_404(Post, id=id)
    photos = PostImages.objects.filter(post=post)
    context = {
        'post': post,
        'photos': photos,

    }
    return render(request, 'web/detail.html', context)
