from django.urls import path
from . import views
urlpatterns = [
    path("tags/",views.TagListView.as_view(),name="tag-list"),
    path("tags/<slug:slug>/",views.TagDetailView.as_view(),name="tag-details"),
    path("startups/",views.StartupListView.as_view(),name="startup-list"),
    path("startups/<slug:slug>/",views.StartupDetailView.as_view(),name="startup-details"),
    path("newslink/",views.NewsLinkAPIList.as_view(),name="newslink-list"),
    path("newslink/<slug:startup_slug>/<slug:newslink_slug>/",views.NewsLinkAPIDetail.as_view(),name="newslink-details"),
    # path("tags/<int:pk>/",views.tag_details,name="tag-detail"),    
]