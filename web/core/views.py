from django.shortcuts import render, get_object_or_404, render_to_response
from django.template import loader
from .models import Post
from .forms import PostForm


# Create your views here.
def index(request):
    submission = PostForm()
    latest_posts = Post.objects.order_by('-pub_date')[:5]
    context = {
        'latest_posts' : latest_posts,
        'submission' : submission
    }

    if request.method == 'POST':
        submission = PostForm(request.POST)
        if submission.is_valid():
            new_post = Post()
            new_post.body = submission.cleaned_data['body']
            new_post.save()
            # return HttpResponseRedirect('core/index.html')

    return render(request, 'core/index.html', context)
    # return render_to_response('core/index.html', context)


def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'core/detail.html', {'post': post})

def about(request):
    return render(request, 'core/about.html')
