from django.urls import path
from . import views
from .views import (PostListView, 
                    PostDetailView, 
                    PostCreateView, 
                    PostUpdateView, 
                    PostDeleteView, 
                    PostListMLBView,
                    PostListNBAView,
                    PostListNFLView)

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('mlb/', PostListMLBView.as_view(), name='blog-mlb'),
    path('nba/', PostListNBAView.as_view(), name='blog-nba'),
    path('nfl/', PostListNFLView.as_view(), name='blog-nfl'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete')
]
       