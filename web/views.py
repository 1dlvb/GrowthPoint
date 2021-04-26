from django.shortcuts import render
from django.templatetags.static import static
# Create your views here.


def index(request):
    logo_gray = static('images/logo_gray.png')
    context = {
        'title': 'Home',
        'logo_gray': logo_gray,
    }
    return render(request, 'web/base.html', context)
