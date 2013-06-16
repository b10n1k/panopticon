from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.contrib.auth.models import User

from panopticon.projects.models import Project, Participant
from panopticon.projects.forms import ProjectForm, ParticipantForm
from panopticon.decorators import is_logged_in


def project_view(request, slug):
    pass


def project_edit(request, slug):
    pass