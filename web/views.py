from django.shortcuts import render
from django.templatetags.static import static
from django.utils import timezone
from .models import Post
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
