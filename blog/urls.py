from django.urls import path
from . import views
urlpatterns = [
    path("blog/",views.BlogPostListAPI.as_view(),name="blogpost-list"),
    path("blog/<int:year>/<int:month>/<slug:slug>/",views.BlogPostAPIDetail.as_view(),name="blogpost-details"),
]