from django.forms import ModelForm, IntegerField
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


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
        labels = {'body': 'Enter a post: ',}
        # help_texts

        def clean_post(self):
            data = self.cleaned_data['body']
            return data

    def __init__(self, *args, **kwargs):
        # propogate post id
        # https://stackoverflow.com/questions/5708650/how-do-i-add-a-foreign-key-field-to-a-modelform-in-django
        # postid = kwargs.pop('post_id', '')
        super(CommentForm, self).__init__(*args, **kwargs)
        # self.fields['post_id'] = postid


