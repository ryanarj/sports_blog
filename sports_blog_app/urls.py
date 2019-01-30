from django.urls import path
from . import views
from .views import (PostListView, 
                    PostDetailView, 
                    PostCreateView, 
                    PostUpdateView, 
                    PostDeleteView, 
                    PostListMLBView,
                    PostListNBAView,
                    PostListNFLView,
                    PostCommentView,
                    PostCommentApproveView,
                    PostCommentRemoveView)

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('mlb/', PostListMLBView.as_view(), name='blog-mlb'),
    path('nba/', PostListNBAView.as_view(), name='blog-nba'),
    path('nfl/', PostListNFLView.as_view(), name='blog-nfl'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/comment/', PostCommentView, name='add_comment_to_post'),
    path('post/<int:pk>/comment/(?P<pk2>[0-9]+)/approve/', PostCommentApproveView, name='comment_approve'),
    path('post/<int:pk>/comment/(?P<pk2>[0-9]+)/remove/', PostCommentRemoveView, name='comment_remove')
]
       