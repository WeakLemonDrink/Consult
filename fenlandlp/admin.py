from django.db import models
from django.contrib import admin
from .models import Post, Comment
from django.conf import settings
from django_summernote.admin import SummernoteModelAdmin

class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    fields = [('title', 'slug'), ('author', 'status'), 'content']
    list_filter = ('status', 'created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

    summernote_fields = ('content',)
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'client', 'body', 'post', 'file', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('user','body',)
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)

admin.site.register(Post, PostAdmin)
