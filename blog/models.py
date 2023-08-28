from django.db import models
from organizer.models import Tag,Startup
from django_extensions.db.models import AutoSlugField
class Post(models.Model):
    title = models.CharField(max_length=63)
    slug = AutoSlugField(max_length=63,unique=True,populate_from=["name"])
    text = models.TextField()
    pub_date = models.DateField()
    tags = models.ManyToManyField(Tag)
    startups = models.ManyToManyField(Startup)
    
    def __str__(self):
        date_string = self.pub_date.strftime("%Y-%m-%d")
        return f"{self.title} on {date_string}"
    
