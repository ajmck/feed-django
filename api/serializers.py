from core.models import Post, Comment
from feed.settings.base import POST_BODY_LENGTH
from rest_framework import serializers
from rest_framework_gis import serializers as geoserializers


class PostAbstractPOSTSerializer(serializers.BaseSerializer):
    body = serializers.CharField(max_length=POST_BODY_LENGTH)
    latitude = serializers.FloatField(required=False)
    longitude = serializers.FloatField(required=False)

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


    # def update(self, instance, validated_data):
    #     pass

    def create(self, validated_data):
        return Post.objects.create(**validated_data)

