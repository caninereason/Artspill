from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from autoslug import AutoSlugField
from django.utils.text import slugify
STATUS = ((0, "Draft"), (1,"Published"))
# Create your models here.





class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(null=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='blogpost_like', blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = original_slug = slugify(self.title)
            for i in range(1, 100):  # we assume less than 100 posts with similar title
                if not Post.objects.filter(slug=self.slug).exists():
                    break
                self.slug = '{}-{}'.format(original_slug, i)
        super().save(*args, **kwargs)

class Comment(models.Model):
    post =models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name= models.CharField(max_length=80)
    email = models.EmailField()
    body =models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
   

    class Meta:
        ordering = ['created_on']
    
    def __str__(self):
        return f"comment {self.body} by {self.name}"

class Favorites(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('user', 'post')  # Prevents the same post from being favorited multiple times by the same user