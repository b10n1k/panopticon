from django.contrib import admin
from panopticon.profiles.models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'email', 'first_name', 'last_name', 'city',
                    'country']

admin.site.register(UserProfile, UserProfileAdmin)