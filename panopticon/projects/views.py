from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.contrib.auth.models import User

from panopticon.profiles.models import UserProfile
from panopticon.projects.models import Project, Participant
from panopticon.projects.forms import ProjectForm, ParticipantForm
from panopticon.decorators import is_logged_in


def project_view(request, slug):
    me = UserProfile.objects.get(user=request.user)
    project = Project.objects.get(slug=slug)
    return render(request, 'project_view.html',
                  {'me': me, 'project': project})


@is_logged_in
def project_edit(request, slug):
    me = UserProfile.objects.get(user=request.user)
    project = Project.objects.get(slug=slug)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('/p/%s/' % slug)
    else:
        form = ProjectForm(instance=project)
    return render(request, 'project_edit_or_create.html',
                  {'me': me, 'form': form})


@is_logged_in
def project_create(request):
    me = UserProfile.objects.get(user=request.user)
    if me.member:
        if request.method == 'POST':
            form = ProjectForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/dashboard/')
        else:
            form = ProjectForm()
    else:
        return redirect('/')
    return render(request, 'project_edit_or_create.html',
                  {'me': me, 'form': form})