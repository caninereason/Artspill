from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic, View
from django.views.generic import ListView, DeleteView
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages

from .models import Post
from .forms import CommentForm, PostForm



class PostDeleteView(View):

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        post.delete()
        messages.success(request, 'Post deleted!')
        return redirect('home')
        


class addPost(View):

    def post(self, request, *args, **kwargs):
        form = PostForm(data=request.POST, files=request.FILES)
        form.instance.author = request.user
        form.instance.author_name = request.user.username
      
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            form = PostForm()
            errormsg = 'Oops, something went wrong!'
            return render(request, "post.html", {'form': form, 'errormsg': errormsg})

    def get(self, request, *args, **kwargs):
        form = PostForm()
        return render(request, "post.html", {'form': form})

    
    # def delete_post(request, pk):
    #     post = get_object_or_404(Post, pk=pk)
    #     if request.method == 'POST':
    #         post.delete()
    #         return redirect('post_list')
    #     return render(request, "delete_post.html", {'post': post})

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
        comments = post.comments.filter(approved=True).order_by('-created_on')
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
            comments = post.comments.filter(approved=True).order_by('-created_on')
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
    