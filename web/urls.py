from django.urls import path, include
from . import views

# Register your models here.
urlpatterns = [
    path('', views.index)
]