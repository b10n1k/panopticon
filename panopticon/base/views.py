from django.shortcuts import render, redirect

from panopticon.profiles.models import UserProfile
from panopticon.projects.models import Project
from panopticon.diavgeia.models import Transaction
from panopticon.decorators import is_logged_in


def index(request):
    if request.user.is_authenticated():
        me = UserProfile.objects.get(user=request.user)
        return render(request, 'index.html', {'me': me})
    return render(request, 'index.html', )


@is_logged_in
def dashboard(request):
    try:
        me = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        return redirect('/u/register/')

    projects = Project.objects.all()
    transactions = Transaction.objects.all()[:20]
    return render(request, 'dashboard.html', {'me': me,
                  'projects': projects, 'transactions': transactions})


def about(request):
    if request.user.is_authenticated():
        me = UserProfile.objects.get(user=request.user)
        return render(request, 'about.html', {'me': me})
    return render(request, 'about.html', )


def contact(request):
    if request.user.is_authenticated():
        me = UserProfile.objects.get(user=request.user)
        return render(request, 'contact.html', {'me': me})
    return render(request, 'contact.html', )
