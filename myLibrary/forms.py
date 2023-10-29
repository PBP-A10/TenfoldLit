
from django.forms import DateField, ModelForm
from django.forms.widgets import DateInput
from .models import BorrowedBooks

class UserBorrowForm(ModelForm):
    class Meta:
        model = BorrowedBooks
        fields = ['date_borrowed', 'date_ended']
        date_borrowed = DateField(
            widget=DateInput(
                attrs={
                    'type': 'date',
                    'placeholder': 'yyyy-mm-dd',
                    'class': 'form-control'
                }
            )
        )

        date_ended = DateField(
            widget=DateInput(
                attrs={
                    'type': 'date',
                    'placeholder': 'yyyy-mm-dd',
                    'class': 'form-control'
                }
            )
        )

        
