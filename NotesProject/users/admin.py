from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Profile

# Register your models here.


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    
    list_display = ('pk','user', 'phone_number','website', 'picture')
    list_display_links = ('pk','user')
    list_editable = ('phone_number', 'picture')
    search_fields = ('user__email', 'user__first_name', 'user__last_name', 'phone_number')
    list_filter = ('create','user__is_active')

    # Para cambiar la edición
    fieldsets = (
        ('Profile', {'fields': (('user', 'picture')), }),
        ('Extra', {'fields': ('phone_number', 'website')}),
        ('Meta', {'fields': ('create', 'modified')}),
    )

    #Campos no editables
    readonly_fields = ('create','modified',)


class ProfileInline(admin.StackedInline):
    
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profiles'


class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)
    

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
