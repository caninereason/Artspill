from .models import Comment, Post
from django import forms

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content','featured_image',]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class PostForm(forms.ModelForm):
    title = forms.CharField(required=True)

    content = forms.CharField(
        widget=forms.widgets.Textarea(
            attrs={
                "placeholder": "Express Yourself",
                
            }
        ),
        label="",
    )

    class Meta:
        model = Post
        exclude = ("user", "author","excerpt", "likes", "slug",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['content'].required = False  # Set excerpt as not required

    