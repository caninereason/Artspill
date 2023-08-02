from . import views
from django.urls import path
from .views import ProfileView, addPost, EditCommentView


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('add', views.addPost.as_view(), name='add'),
    path('delete/<slug>', views.PostDeleteView.as_view(), name='delete_post'),
    path('edit/<slug:slug>/', views.EditPostView.as_view(), name='edit_post'),
    path('profile', ProfileView.as_view(), name='profile'),
    path('edit_comment/<int:comment_id>/', EditCommentView.as_view(), name='edit_comment'),
    path('add_to_favorites/<int:post_id>/', views.AddToFavoritesView.as_view(), name='add_to_favorites'),
    
    # path('profile/<user>/', views.ProfileView.as_view(), name='profile'),
    # path('delete_post', views.PostDeleteView.as_view(), name='post_delete'),
]