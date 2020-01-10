from django.forms import ModelForm, Textarea
from django import forms
from .models import Email, Contact

class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
    
    

class EmailForm(forms.Form):
    class Meta:
        model = Email
        fields = ('name', 'Subject', 'message')