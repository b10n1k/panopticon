from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.contrib.auth.models import User

from panopticon.base.models import UserProfile
from panopticon.base.forms import UserProfileForm
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
        display_name = request.user
        return redirect('/register/')
    return render(request, 'dashboard.html', {'me': me})


@is_logged_in
def register(request):
    try:
        me = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        if request.method == 'POST':
            me = User.objects.get(username=request.user)
            form = UserProfileForm(request.POST)
            if form.is_valid():
                f = form.save(commit=False)
                f.user = me
                f.email = me.email
                form.save()
                return redirect('/dashboard/')
        else:
            form = UserProfileForm()
    return render(request, 'profile_edit_or_create.html', locals())


@is_logged_in
def profile_view(request, slug):
    me = get_object_or_404(UserProfile.objects.filter(display_name=slug))
    return render(request, 'profile_view.html', {'me': me})


@is_logged_in
def profile_edit(request, slug):
    me = UserProfile.objects.get(user=request.user)
    if me.display_name != slug:
        return redirect('/dashboard/')
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=me)
        if form.is_valid():
            form.save()
            return redirect('/dashboard/')
    else:
        form = UserProfileForm(instance=me)
    return render(request, 'profile_edit_or_create.html', locals())


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
