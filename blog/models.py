from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import MinLengthValidator

# Create your models here.

class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return self.caption


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(null=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Post(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(default="", unique=True, db_index=True)
    image = models.ImageField(upload_to="posts", null=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    date = models.DateField(auto_now=True)
    author = models.ForeignKey(
        Author, on_delete=models.SET_NULL, related_name="posts", null=True
        )
    tags = models.ManyToManyField(Tag)

    def get_absolute_url(self):
        return reverse("post", args=[self.slug])

    def __str__(self):
        return f"{self.title} : {self.author}"


class Comment(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    text = models.TextField(max_length=400)
    post = models.ForeignKey(Post, models.CASCADE, related_name="comment")