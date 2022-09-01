from django.urls import path
from Ideablog import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, UserPostListView, PostDeleteView
urlpatterns = [
    path('', views.index_page, name='index_page'),
    path('home', PostListView.as_view(), name='blog-home'),
    path('user/<username>', UserPostListView.as_view(), name='user-posts'),
     path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
     path('post/new/', PostCreateView.as_view(), name='post-create'),
      path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
     path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('donate/', views.donate, name='donate'),
    path('Terms and conditions/', views.termsconditions, name='t&c'),
] 
