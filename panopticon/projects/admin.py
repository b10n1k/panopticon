from django.contrib import admin
from panopticon.projects.models import Project, Participant


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'active']

admin.site.register(Project, ProjectAdmin)


class ParticipantAdmin(admin.ModelAdmin):
    list_display = ['user', 'owner']

admin.site.register(Participant, ParticipantAdmin)