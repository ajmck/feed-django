from core.models import Post, Comment, Meshblock
from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer


class MeshblockSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Meshblock
        geo_field = "geom"
        fields = "__all__"


class PostSerializer(serializers.HyperlinkedModelSerializer):
    total_upvotes  = serializers.IntegerField(read_only=True)
    total_downvotes = serializers.IntegerField(read_only=True)
    vote_total = serializers.IntegerField(read_only=True)

    class Meta:
        model = Post
        # fields = '__all__'
        exclude = ['moderation']

    def create(self, validated_data):
        return Post.objects.create(**validated_data)