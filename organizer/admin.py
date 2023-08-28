from django.contrib import admin
from .models import Startup,Tag,NewsLink
# Register your models here.

class TagAdmin(admin.ModelAdmin):
    list_display = ('name','slug')

admin.site.register(NewsLink)
admin.site.register(Startup)
admin.site.register(Tag,TagAdmin)

