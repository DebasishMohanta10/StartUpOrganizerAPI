from rest_framework.serializers import ModelSerializer,SerializerMethodField

from rest_framework.reverse import reverse
from organizer.serializers import TagSerializer,StartupSerializer
from .models import Post

class BlogPostSerializer(ModelSerializer):
    url = SerializerMethodField()
    tags = TagSerializer(many=True)
    startups = StartupSerializer(many=True)
    class Meta:
        model = Post
        fields = "__all__"
        
    def get_url(self, post):
        """Return full API URL for serialized POST object"""
        return reverse(
            "api-post-detail",
            kwargs=dict(
                year=post.pub_date.year,
                month=post.pub_date.month,
                slug=post.slug,
            ),
            request=self.context["request"],
        )