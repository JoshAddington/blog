from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm, CommentForm


def index(request):
        return render(request, 'index.html')


def post_list(request):
        # filter unpublished posts
        posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
        return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
        post = get_object_or_404(Post, pk=pk)
        projects_length = len(post.project.all())
        form = CommentForm(request.POST or None)
        if form.is_valid():
                comment = form.save(commit=False)
                comment.post = post
                comment.save()
                return redirect(request.path)
        return render(request, 'blog/post_detail.html', {'post': post, 'projects_length': projects_length, 'form': form})


