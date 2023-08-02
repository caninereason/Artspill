from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin
from .forms import PostForm

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):  # Inherit from SummernoteModelAdmin
    
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    summernote_fields = ('content',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on')
    list_filter = ('created_on',)
    search_fields = ['name', 'email', 'body']
    actions = ['delete_comments']  # Rename the action to 'delete_comments'

    

    