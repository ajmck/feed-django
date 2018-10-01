from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, render_to_response
from django.template import loader
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.contrib.gis.geos import Point
from secretballot.views import vote
from feed.settings.base import GOOGLE_ANALYTICS_KEY


# Create your views here.
def index(request):
    if request.method == 'POST':
        submission = PostForm(request.POST)

        if submission.is_valid():
            new_post = Post()
            new_post.body = submission.cleaned_data['body']

            try:
                lat = float(submission.data['latitude'])
                lon = float(submission.data['longitude'])
                if lat is not None and lon is not None:
                    # What the FUCK
                    # Points require longitude before latitude
                    # https://stackoverflow.com/questions/30823988/geodjango-converting-srid-4326-to-srid-3857
                    new_post.post_location = Point(x=lon, y=lat)
            except Exception as e:
                print(e)
                new_post.post_location = None

            new_post.save()
            return HttpResponseRedirect('/')

    submission = PostForm()
    latest_posts = Post.objects.order_by('-pub_date')
    context = {
        'latest_posts' : latest_posts,
        'submission' : submission,
        'GA_KEY': GOOGLE_ANALYTICS_KEY
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

            try:
                lat = float(submission.data['latitude'])
                lon = float(submission.data['longitude'])
                if lat is not None and lon is not None:
                    # What the FUCK
                    # Points require longitude before latitude
                    # https://stackoverflow.com/questions/30823988/geodjango-converting-srid-4326-to-srid-3857
                    new_comment.post_location = Point(x=lon, y=lat)
            except Exception as e:
                print(e)
                new_comment.post_location = None

            new_comment.body = submission.cleaned_data['body']
            new_comment.save()
            return HttpResponseRedirect('/' + str(post_id))

    submission = CommentForm()
    # comments_fk is the related name of parent, in the comments class
    comments = post.comments_fk.all()
    context = {
        'post': post,
        'submission': submission,
        'comments': comments,
        'GA_KEY': GOOGLE_ANALYTICS_KEY
    }

    return render(request, 'detail.html', context)


def location(request):
    context = {
        'GA_KEY': GOOGLE_ANALYTICS_KEY
    }
    return render(request, 'location.html', context)


def classic(request):
    context = {
        'GA_KEY': GOOGLE_ANALYTICS_KEY
    }
    return render(request, 'classic.html', context)


def about(request):
    context = {
        'GA_KEY': GOOGLE_ANALYTICS_KEY
    }
    return render(request, 'about.html', context)


def post_vote_up(request, post_id):
    return vote(request, Post, post_id, +1, redirect_url=request.META.get('HTTP_REFERER'))


def post_vote_down(request, post_id):
    return vote(request, Post, post_id, -1, redirect_url=request.META.get('HTTP_REFERER'))


def post_vote_reset(request, post_id):
    return vote(request, Post, post_id, 0, redirect_url=request.META.get('HTTP_REFERER'))


def comment_vote_up(request, comment_id):
    return vote(request, Comment, comment_id, +1, redirect_url=request.META.get('HTTP_REFERER'))


def comment_vote_down(request, comment_id):
    return vote(request, Comment, comment_id, -1, redirect_url=request.META.get('HTTP_REFERER'))


def comment_vote_reset(request, comment_id):
    return vote(request, Comment, comment_id, 0, redirect_url=request.META.get('HTTP_REFERER'))
