from django.urls import path
from . import views

app_name = 'posts'  # This defines the namespace

urlpatterns = [
    path('', views.posts_list, name="list"),
    path('<slug:slug>', views.post_page, name="page"),
]
