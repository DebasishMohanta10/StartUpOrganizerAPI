from django.shortcuts import get_object_or_404
from .serializers import BlogPostSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import Post
class BlogPostListAPI(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = BlogPostSerializer
    
class BlogPostAPIDetail(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = BlogPostSerializer
    
    def get_object(self):
        month = self.kwargs.get("month")
        year = self.kwargs.get("year")
        slug = self.kwargs.get("slug")
        
        queryset = self.filter_queryset(self.get_queryset())
        
        post = get_object_or_404(queryset,pub_date__year=year,pub_date__month=month,slug=slug)
        
        self.check_object_permissions(self.request, post)
        return post
