from django.urls import path
from .views import PostListView, PostDetailView

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),  # List all posts
    path('<int:pk>/', PostDetailView.as_view(), name='post-detail'),  # Detail view for a single post
]
