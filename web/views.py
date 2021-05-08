from django.shortcuts import render, get_object_or_404
from django.templatetags.static import static
from django.utils import timezone
from .models import Post, PostAdditionalImages\

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


def detail_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    data = PostAdditionalImages.objects.filter(post=post)
    images = []
    text = []
    for data1 in data:
        images.append(data1.image)
        text.append(data1.text)

    context = {
        'post': post,
        'photos': images,
        'text': text,
        'queryset': data,
    }
    return render(request, 'web/detail.html', context)
