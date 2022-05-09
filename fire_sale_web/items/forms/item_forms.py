from django.forms import ModelForm, widgets
from django import forms
from items.models import Item


class ItemCreateForm(ModelForm):
    image = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Item
        exclude = {'id'}
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'description': widgets.TextInput(attrs={'class': 'form-control'}),
            'category': widgets.Select(attrs={'class': 'form-control'}),
            'on_sale': widgets.CheckboxInput(attrs={'class': 'form-control'}),
                'price': widgets.NumberInput(attrs={'class': 'form-control'}),
            'user': widgets.Select(attrs={'class': 'form-control'})
        }

