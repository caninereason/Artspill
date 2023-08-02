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
import cloudinary.uploader




class EditCommentView(LoginRequiredMixin, View):
    template_name = 'edit_comment.html'

    def get(self, request, comment_id):
        # Retrieve the comment based on the comment_id or return 404 if not found
        comment = get_object_or_404(Comment, id=comment_id)
        return render(request, self.template_name, {'comment': comment})

    def post(self, request, comment_id):
        # Retrieve the comment based on the comment_id or return 404 if not found
        comment = get_object_or_404(Comment, id=comment_id)

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
        comments = Comment.objects.filter(post__in=posts).order_by('-created_on')
        print(f"User: {request.user.username}")
        print(f"Number of posts: {posts.count()}")
        print(f"Number of comments: {comments.count()}")

        # Display debug information in messages
        messages.info(request, f"User: {request.user.username}")
        messages.info(request, f"Number of posts: {posts.count()}")
        messages.info(request, f"Number of comments: {comments.count()}")

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

class PostLike(View):

    def post(self,request,slug, *args, **kwargs):
        post = get_object_or_404(Post,slug=slug)

        if post.likes.filter(id=request.user.id).exists():
             post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
        
        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6

    

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
        Favorites.objects.get_or_create(user=request.user, post=post)  # Creates a favorite, or does nothing if it already exists
        return redirect('home')



    