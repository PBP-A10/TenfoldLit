from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'style':'margin-top: 10px; margin-bottom: 10px'}))
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    
    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['style'] = 'margin-top: 10px; margin-bottom: 10px'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['style'] = 'margin-top: 10px; margin-bottom: 10px'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['style'] = 'margin-top: 10px; margin-bottom: 15px'