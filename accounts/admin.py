from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from accounts.models import Organisation, Client

from .models import Profile

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )
    list_display = ('username',
                    'email',
                    'first_name',
                    'last_name',
                    'is_staff')
    list_select_related = ('profile', )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)
    

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
                    'agent')      


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)