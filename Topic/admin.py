from django.contrib import admin
from .models import Topic, Entry, UserProfile, Subscribe
from django.contrib.auth.models import User


admin.site.site_header = 'Learning Log Administration'
admin.site.site_title = 'Learning Log'
admin.site.index_title = 'Welcome to Learning Log Administration'


@admin.register(UserProfile)
class AdminUserProfile(admin.ModelAdmin):
    list_display = ['user', 'image', 'bio']

class  EntryInline(admin.TabularInline):
    model = Entry
    extra = 1
    
    
@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'image', 'user']
    fieldsets = [(None, {'fields': ['title', 'image']}),]
    inlines = [EntryInline]




# Register your models here.
admin.site.register(Subscribe)