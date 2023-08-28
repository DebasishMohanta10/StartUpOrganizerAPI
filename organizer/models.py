from django.db import models
from django_extensions.db.models import AutoSlugField
class Tag(models.Model):
    name = models.CharField(max_length=31,unique=True)
    slug = AutoSlugField(max_length=31,unique=True,help_text="A Label for URL config",populate_from=["name"])
    
    def __str__(self):
        return self.name
    
class Startup(models.Model):
    name = models.CharField(max_length=63,db_index=True)
    slug = AutoSlugField(max_length=63,unique=True,populate_from=["name"])
    description = models.TextField()
    founded_date = models.DateField("Date Founded")
    contact = models.EmailField()
    website = models.URLField(max_length=255)
    tags = models.ManyToManyField(Tag)
    
    def __str__(self):
        return self.name

class NewsLink(models.Model):
    title = models.CharField(max_length=31)
    slug = AutoSlugField(max_length=31,unique=True,populate_from=["title"])
    pub_date = models.DateField()
    link = models.URLField(max_length=255)
    startup = models.ForeignKey(Startup,on_delete=models.CASCADE)
    
    def __str__(self):  
        return f"{self.startup}: {self.title}"
    