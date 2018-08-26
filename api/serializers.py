from core.models import Post, Comment
from feed.settings.base import POST_BODY_LENGTH
from rest_framework import serializers


class PostSerializer(serializers.Serializer):
    body = serializers.CharField(max_length=POST_BODY_LENGTH)
    pub_date = serializers.DateTimeField(required=False)

    # def update(self, instance, validated_data):
    #     pass

    def create(self, validated_data):
        return Post.objects.create(**validated_data)

