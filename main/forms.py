from django import forms
from.models import ContactForm,Buy

class ContactFormForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['name', 'email', 'message']
class BuyForm(forms.ModelForm):
    class Meta:
        model=Buy
        fields=['email']