# from django.forms.models import model_to_dict
# from django.http import JsonResponse,Http404
from django.shortcuts import get_object_or_404
from .models import Tag,Startup,NewsLink
from rest_framework.views import APIView
from .serializers import TagSerializer,StartupSerializer,NewsLinkSerializer
from rest_framework.response import Response
from rest_framework import generics

# class TagListView(APIView):
#     def get(self , request ):
#         tags =Tag.objects.all()
#         serialized_tags = TagSerializer(tags,many=True)
#         return Response(serialized_tags.data)
    
#     def post(self,request):
#         serialized_tag = TagSerializer(data=request.data)
#         serialized_tag.is_valid(raise_exception=True)
#         serialized_tag.save()
#         return Response(serialized_tag.data)

class TagListView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class TagDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    lookup_field = 'slug'
    # lookup_url_kwarg = 'slug'

class StartupListView(generics.ListCreateAPIView):
    queryset = Startup.objects.all()
    serializer_class=StartupSerializer
    
class StartupDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Startup.objects.all()
    serializer_class = StartupSerializer
    lookup_field = 'slug'
    
class NewsLinkAPIList(generics.ListCreateAPIView):
    queryset = NewsLink.objects.all()
    serializer_class = NewsLinkSerializer
    
class NewsLinkAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = NewsLink.objects.all()
    serializer_class = NewsLinkSerializer
    # lookup_field = 'slug'
    # lookup_url_kwarg = "newslink_slug"
    
    def get_object(self):
        startup_slug = self.kwargs.get("startup_slug")
        newslink_slug = self.kwargs.get("newslink_slug")
        
        queryset = self.filter_queryset(self.get_queryset())
        

        newslink = get_object_or_404(queryset,slug=newslink_slug,startup__slug=startup_slug)

        # May raise a permission denied
        self.check_object_permissions(self.request, newslink)

        return newslink
    