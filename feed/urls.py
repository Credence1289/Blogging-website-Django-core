from django.urls import path
from .views import  PostDetailView, PostCreateView,UserPostListView,PostUpdateView, PostDeleteView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:id>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:id>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:id>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<str:username>/', UserPostListView.as_view(), name='user-post-list'),
    path('search/', views.search, name='search'),
]

'''
Home
About
PostListView
UserPostListView
PostCreateView
PostDetailView
PostUpdateView
PostDeleteView
Search
'''