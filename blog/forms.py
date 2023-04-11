from .models import Comment, Post
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class PostForm(forms.ModelForm):
    title = forms.CharField(required=True)
    
   
    
    content =forms.CharField(
         widget=forms.widgets.Textarea(

            attrs={

                "placeholder": "Express Yourself",
                          }
        ),
        label="",
    )
    


    class Meta:

        model = Post

        exclude = ("user","slug", "author", "status", "likes","excerpt",)