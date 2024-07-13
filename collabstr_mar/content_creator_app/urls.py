from django.urls import path

from . import views

urlpatterns = [
    path('', views.content_list, name='content_list'),
    path('filter/', views.filter_by_platform, name='filter_by_platform'),
]