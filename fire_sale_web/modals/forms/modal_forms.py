from django import forms

class OfferForm(forms.Form):
    username = forms.CharField(label="username", required=True, max_length=10)
    number = forms.IntegerField(label="number", required=True)