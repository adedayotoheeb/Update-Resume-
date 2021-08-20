from django import forms
from django.forms import ModelForm
from django.core import validators
from .models import *

class ContactForm(forms.ModelForm):
    name = forms.CharField( label='Name', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}))
    message = forms.CharField(label='Message',widget= forms.Textarea(attrs={'placeholder':'Message','class':'form-control'}))
    botcatcher = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta():
        model = Contact
        fields = ('name', 'email', 'message')

    def clean_botcatcher(self):
        botcatcher = self.cleaned_data['botcatcher']
        if len(botcatcher) > 0:
            raise forms.ValidationError("Please Fill The Form Manually")
        return botcatcher