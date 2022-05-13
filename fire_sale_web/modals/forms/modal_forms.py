from django import forms

class OfferForm(forms.Form):
    offer = forms.IntegerField(label="number", required=True)