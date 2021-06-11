from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index),
    path('contact/', views.contact, name='contact'),
    path('where/', views.where, name='where'),
    path('team/', views.our_team, name='team'),
    path('post/<int:pk>/', views.detail_view, name='detail'),

]