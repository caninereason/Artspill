from . import views
from django.urls import path
from .views import ProfileView


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('add', views.addPost.as_view(), name='add'),
    path('delete/<slug>', views.PostDeleteView.as_view(), name='delete_post'),
    path('edit/<slug:slug>/', views.EditPostView.as_view(), name='edit_post'),
    path('profile', ProfileView.as_view(), name='profile'),
    # path('profile/<user>/', views.ProfileView.as_view(), name='profile'),
    # path('delete_post', views.PostDeleteView.as_view(), name='post_delete'),
]