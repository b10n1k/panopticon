from django.forms import ModelForm, RadioSelect
from panopticon.diavgeia.models import Transaction


class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        widgets = {
            'category': RadioSelect,
        }