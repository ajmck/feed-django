from django.forms import ModelForm
from .models import Post, Comment


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['body']
        labels = {'body': 'Enter a post: ',}
        # help_texts

        def clean_post(self):
            data = self.cleaned_data['body']
            return data


class CommentForm(PostForm):
    class Meta(PostForm.Meta):
        model = Comment
