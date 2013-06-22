from django.forms import Form, ModelForm, ChoiceField, RadioSelect
from panopticon.projects.models import Project, Participant


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        exclude = ('active', 'slug',)


class ParticipantForm(ModelForm):
    class Meta:
        model = Participant