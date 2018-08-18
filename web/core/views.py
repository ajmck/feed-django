from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, render_to_response
from django.template import loader
from .models import Post, Comment
from .forms import PostForm, CommentForm


# Create your views here.
def index(request):
    if request.method == 'POST':
        submission = PostForm(request.POST)
        if submission.is_valid():
            new_post = Post()
            new_post.body = submission.cleaned_data['body']
            new_post.save()
            return HttpResponseRedirect('/')

    submission = PostForm()
    latest_posts = Post.objects.order_by('-pub_date')
    context = {
        'latest_posts' : latest_posts,
        'submission' : submission
    }
    return render(request, 'index.html', context)
    # return render_to_response('core/index.html', context)


def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == 'POST':
        submission = CommentForm(request.POST)
        if submission.is_valid():
            new_comment = Comment()
            new_comment.parent = post
            new_comment.body = submission.cleaned_data['body']
            new_comment.save()
            return HttpResponseRedirect('/' + str(post_id))

    submission = CommentForm()
    # parent_post is the related name of parent, in the comments class
    comments = post.parent_post.all()
    context = {
        'post': post,
        'submission': submission,
        'comments': comments
    }

    return render(request, 'detail.html', context)


def location(request):
    return render(request, 'location.html')
