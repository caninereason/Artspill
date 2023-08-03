from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic, View
from django.views.generic import ListView, DeleteView
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import  Post, Comment, Favorites
from .forms import CommentForm, PostForm, EditForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import models
from django.contrib.auth.forms import UserChangeForm
import cloudinary.uploader
from django.http import HttpResponseForbidden


class EditUserView(LoginRequiredMixin, View):
    template_name = 'edit_user.html'

    def get(self, request):
        form = UserChangeForm(instance=request.user)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
        return render(request, self.template_name, {'form': form})

class EditCommentView(LoginRequiredMixin, View):
    template_name = 'edit_comment.html'

    def get(self, request, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)
        if request.user.username != comment.name:
            return HttpResponseForbidden("You are not allowed to edit this comment.")
        return render(request, self.template_name, {'comment': comment})

    def post(self, request, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)
        if request.user.username != comment.name:
            return HttpResponseForbidden("You are not allowed to edit this comment.")

        new_comment_text = request.POST.get('comment_text')
        if new_comment_text:
            comment.body = new_comment_text
            comment.save()
        # You may add a success message here if desired
        return redirect('profile')

class ProfileView(LoginRequiredMixin, View):
    template_name = 'profile.html'

    def get(self, request, *args, **kwargs):
        # Filter the posts that belong to the currently authenticated user,
        # and order them by the `created_on` field in descending order
        posts = Post.objects.filter(author=request.user).order_by('-created_on')
        favorites = Favorites.objects.filter(user=request.user)
        # Collect all the comments for the user's posts
        comments = Comment.objects.filter(name=request.user.username).order_by('-created_on')
       
        return render(request, self.template_name, {'posts': posts, 'favorites': favorites, 'comments': comments})



class EditPostView(View):
    model = Post
    form_class = PostForm
    template_name = 'post.html'

    

    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        form = self.form_class(request.POST or None, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', slug=post.slug)
        else:
            form = self.form_class(instance=post) # re-initialize the form with the instance if it's not valid
        return render(request, self.template_name, {'form': form, 'post': post})





class PostDeleteView(View):

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        post.delete()
        messages.success(request, 'Post deleted!')
        return redirect('home')
        






class addPost(View):
    model = Post

    def post(self, request, *args, **kwargs):
        form = PostForm(data=request.POST, files=request.FILES)
        form.instance.author = request.user
        form.instance.author_name = request.user.username
        if form.is_valid():
            post = form.save(commit=False)
            if 'featured_image' in request.FILES:
                image = request.FILES['featured_image']
                cloudinary_response = cloudinary.uploader.upload(image)
                post.featured_image = cloudinary_response['secure_url']
            post.save()
            return redirect('post_detail', slug=post.slug)  # Here, add the slug argument
        else:
            errormsg = 'Oops, something went wrong!'
            return render(request, "post.html", {'form': form, 'errormsg': errormsg})

    # the rest of your methods


    def get(self, request, *args, **kwargs):
        form = PostForm()
        return render(request, "post.html", {'form': form})

    def edit_post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        form = EditForm(request.POST or None, instance=post, initial={'title': post.title, 'comment': post.comment})
    
        if form.is_valid():
            form.save()
            return redirect('post_detail', slug=post.slug)
        return render(request, 'post.html', {'form': form, 'post': post})

    
    def delete_post(request, pk):
        post = get_object_or_404(Post, pk=pk)
        if request.method == 'POST':
            post.delete()
            return redirect('post_list')
        return render(request, "delete_post.html", {'post': post})





class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        # Check if the user is authenticated
        if user.is_authenticated:
            # If the user is authenticated, get the list of liked post IDs
            liked_posts = Favorites.objects.filter(user=user).values_list('post__id', flat=True)
        else:
            # If the user is not authenticated, set liked_posts to an empty list
            liked_posts = []

        context['liked_posts'] = liked_posts
        return context

    

class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.order_by('-created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked =True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented" :False,
                "liked":liked,
                "comment_form": CommentForm()
            },
        )
    def post(self, request, slug, *args, **kwargs):

            queryset = Post.objects.filter(status=1)
            post = get_object_or_404(queryset, slug=slug)
            comments = post.comments.order_by('-created_on')
            liked = False
            if post.likes.filter(id=self.request.user.id).exists():
                liked =True

            comment_form = CommentForm(data=request.POST)

            if comment_form.is_valid():
                comment_form.instance.email = request.user.email
                comment_form.instance.name = request.user.username
                comment = comment_form.save(commit=False)
                comment.post = post
                comment.save()
            else:
                comment_form = CommentForm()


            return render(
                request,
                "post_detail.html",
                {
                    "post": post,
                    "comments": comments,
                    "commented" :True,
                    "comment_form": CommentForm(),
                    "liked":liked
                    
                },

    
            )

class AddToFavoritesView(View):
    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        try:
            favorite = Favorites.objects.get(user=request.user, post=post)
        except Favorites.DoesNotExist:
            favorite = None

        if favorite:
            # If the post is favorited, remove it from favorites
            favorite.delete()
        else:
            # If the post is not favorited, add it to favorites
            Favorites.objects.create(user=request.user, post=post)

        next_page = request.POST.get('next', '/')
        return HttpResponseRedirect(next_page)

class PostLike(View):

    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)

        # Check if the user liked the post
        if post.likes.filter(id=request.user.id).exists():
            # Unlike the post if the user has already liked it
            post.likes.remove(request.user)
        else:
            # Like the post if the user has not already liked it
            post.likes.add(request.user)

        # Update the number_of_likes field based on the number of users who liked the post
        post.number_of_likes = post.likes.count()

        # Check if the post is favorited by the user
        try:
            favorite = Favorites.objects.get(user=request.user, post=post)
        except Favorites.DoesNotExist:
            favorite = None

        if favorite:
            # If the post is favorited, remove it from favorites
            favorite.delete()
        else:
            # If the post is not favorited, add it to favorites
            Favorites.objects.create(user=request.user, post=post)

        # Update the number_of_favorites field based on the number of users who favorited the post
        post.number_of_favorites = Favorites.objects.filter(post=post).count()

        # Save the changes to the post model
        post.save()

        # Return to the previous page (or post_detail page as a fallback)
        return redirect(request.META.get('HTTP_REFERER', reverse('post_detail', args=[slug])))



    