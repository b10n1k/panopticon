from django.forms import Form, ModelForm, ChoiceField, RadioSelect
from panopticon.profiles.models import UserProfile


class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user', 'email')