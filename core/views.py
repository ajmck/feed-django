from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, render_to_response
from django.template import loader

from core.models import Meshblock
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.contrib.gis.geos import Point
from secretballot.views import vote
from django.conf import settings


# Helper method to propagate environment variables
def create_context(c=None):
    default_context = {
        'GA_KEY': settings.GOOGLE_ANALYTICS_KEY,
        'ENABLE_LOCATION': settings.ENABLE_LOCATION,
        'ENABLE_DISCLAIMER': settings.ENABLE_DISCLAIMER,
    }

    if c is None:
        return default_context
    else:
        return {**default_context, **c}


# helper method to save location in posts
def add_location(post, submission):
    try:
        lat = float(submission.data['latitude'])
        lon = float(submission.data['longitude'])
        if lat is not None and lon is not None:
            # What the FUCK
            # Points require longitude before latitude
            # https://stackoverflow.com/questions/30823988/geodjango-converting-srid-4326-to-srid-3857
            post.post_location = Point(x=lon, y=lat)

            try:
                mesh = Meshblock.objects.get(geom__contains=post.post_location)
            except Meshblock.DoesNotExist:
                mesh = None
                # the other one to catch would be Meshblock.MultipleObjectsReturned
            finally:
                post.post_meshblock = mesh

    except Exception as e:
        print(e)
        post.post_location = None

    return post


# Create your views here.
def index(request):
    if request.method == 'POST':
        submission = PostForm(request.POST)

        if submission.is_valid():
            new_post = Post()
            new_post.body = submission.cleaned_data['body']
            new_post = add_location(new_post, submission)
            new_post.save()
            return HttpResponseRedirect('/')

    submission = PostForm()
    latest_posts = Post.objects.order_by('-pub_date')

    context = create_context({'latest_posts': latest_posts, 'submission': submission})
    return render(request, 'index.html', context)
    # return render_to_response('core/index.html', context)


def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == 'POST':
        submission = CommentForm(request.POST)
        if submission.is_valid():
            new_comment = Comment()
            new_comment.parent = post
            new_comment = add_location(new_comment, submission)
            new_comment.body = submission.cleaned_data['body']
            new_comment.save()
            return HttpResponseRedirect('/' + str(post_id))

    submission = CommentForm()
    # comments_fk is the related name of parent, in the comments class
    comments = post.comments_fk.all()
    context = create_context({
        'post': post,
        'submission': submission,
        'comments': comments,
    })
    return render(request, 'detail.html', context)


def classic(request):
    return render(request, 'classic.html', create_context(None))


def about(request):
    return render(request, 'about.html', create_context(None))


def here(request):
    context = create_context({
        'HERE_APP_ID': settings.HERE_APP_ID,
        'HERE_APP_CODE': settings.HERE_APP_CODE
    })
    return render(request, 'here.html', context)


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
