from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from .models import Post
from django.views import View
from django.views.generic import DetailView, ListView, CreateView
from .forms import CommentForm
from django.http import HttpResponseRedirect

class IndexView(ListView):
    template_name = "blog/index.html"
    model = Post
    context_object_name = "posts"
    ordering = ["-date"]

    def get_queryset(self):
        base = super().get_queryset()
        data = base[:3]
        return data



class PostsView(ListView):
    template_name = "blog/posts.html"
    model = Post
    context_object_name = "all_posts"
    ordering = ["-date"]


class PostView(View):

    def is_stored_post(self, request, post_id):
        stored_posts = request.session.get("stored_posts")

        if stored_posts is not None:
            is_saved_for_later = post_id in stored_posts
        else:
            is_saved_for_later = False 
        
        return is_saved_for_later 

    def get(self, request, slug):
        post = Post.objects.get(slug=slug)

        context = {
            "post" : post,
            "tags" : post.tags.all(),
            "comment_form" :CommentForm(),
            "saved_for_later" : self.is_stored_post(request, post.id),
            "comments" : post.comment.all().order_by("-id")
        }
        return render(request, "blog/post-detail.html", context)

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse("post", args=[slug]))
        
        favorite_slug = request.session.get("favorite_post")
        context = {
            "post" : post,
            "tags" : post.tags.all(),
            "comment_form" :CommentForm(),
            "is_favorite" : favorite_slug == post.slug,
            "comments" : post.comment.all().order_by("-id")
        }
        return render(request, "blog/post-detail.html", context)


class ReadLater(View):

    def get(self, request):
        stored_posts = request.session.get("stored_posts")
        context = {}

        if stored_posts is None or len(stored_posts) == 0:
            context["posts"] = []
            context["has_posts"] = False
        else:
            posts = Post.objects.filter(id__in=stored_posts)
            context["posts"] = posts
            context["has_posts"] = True
        
        return render(request, "blog/stored_posts.html", context)

    def post(self, request): 
        stored_posts = request.session.get("stored_posts")

        if stored_posts is None:
            stored_posts  = []

        post_id = int(request.POST["post_id"])
        post = get_object_or_404(Post, id=post_id)
        if post_id not in stored_posts:
            stored_posts.append(post_id)
        else:
            stored_posts.remove(post_id)
        request.session["stored_posts"] = stored_posts

        return redirect("post", slug=post.slug)
    
    