from rest_framework import serializers
from .models import Tag,Startup,NewsLink
from rest_framework.serializers import SerializerMethodField
from rest_framework.reverse import reverse

class TagSerializer(serializers.HyperlinkedModelSerializer):
    # url = HyperlinkedIdentityField(view_name="tag-details",lookup_field='slug')
    class Meta:
        model = Tag
        fields = "__all__"
        extra_kwargs = {
            "url": {
                "lookup_field": 'slug',
                'view_name': 'tag-details'
            }
        }

class StartupSerializer(serializers.HyperlinkedModelSerializer):
    tags = TagSerializer(many=True)
    # tags_ids = serializers.ListField(write_only=True)
    class Meta:
        model = Startup
        fields = "__all__"
        extra_kwargs = {
            "url": {
                "lookup_field": 'slug',
                "view_name": 'startup-details'
            }
        }

    # def create(self, validated_data):
    #     tags_ids = validated_data.pop('tags_ids',[])
    #     startup = Startup.objects.create(**validated_data)
    #     for tags_id in tags_ids:
    #         tag = Tag.objects.get(pk=tags_id)
    #         startup.tags.add(tag)
    #     return startup
    
class NewsLinkSerializer(serializers.ModelSerializer):
    url = SerializerMethodField()
    startup = StartupSerializer()
    class Meta:
        model = NewsLink
        # fields = "__all__"
        exclude =("id",)
        
    def get_url(self,newslink):
        return reverse(
            "newslink-details",
            kwargs=dict(
                startup_slug=newslink.startup.slug,
                newslink_slug=newslink.slug,
            ),
            request=self.context["request"],
        )