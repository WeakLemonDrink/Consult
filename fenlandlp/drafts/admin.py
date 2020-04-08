from django.db import models
from django.contrib import admin
from .models import Post, Comment
from accounts.models import UserProfile, Organisation, Client
from django.contrib.auth.models import User
from django.conf import settings
from django_summernote.admin import SummernoteModelAdmin

#from django.contrib.auth.admin import UserAdmin

class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    fields = [('title', 'slug'), ('author', 'status'), 'content']
    list_filter = ('status', 'created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

    summernote_fields = ('content',)
    
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user',
                    'alt_id',
                    'position',
                    'organisation',
                    'house_name_no',
                    'street',
                    'town',
                    'county',
                    'postcode',
                    'tel',
                    )
                    
    list_filter = ('organisation',
                   'house_name_no',)
                   
    search_fields = ('position',
                    'organisation',
                    'house_name_no',
                    'street',
                    'town',
                    'county',
                    'postcode',
                     )
    
@admin.register(Organisation)
class OrganisationAdmin(admin.ModelAdmin):
    list_display = ('org_name',
                    'org_id',
                    )                    
    

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('client_first_name',
                    'client_last_name',
                    'client_org',
                    'client_email',
                    'agent')      

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'client', 'body', 'post', 'file', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('user','body',)
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


admin.site.register(Post, PostAdmin)
