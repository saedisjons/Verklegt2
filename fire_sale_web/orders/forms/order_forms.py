from django.forms import ModelForm, widgets
from orders.models import PaymentDetails, ContactInfo, Rating


class PaymentDetailsForm(ModelForm):
    class Meta:
        model = PaymentDetails
        exclude = {'user'}
        widgets = {
            'nameOfCardH': widgets.TextInput(attrs={'class': 'form-control'}),
            'cardNum': widgets.NumberInput(attrs={'class': 'form-control'}),
            'expDate': widgets.DateInput(attrs={'class': 'form-control'}),
            'cvv': widgets.NumberInput(attrs={'class': 'form-control'}),
        }


class ContactInfoForm(ModelForm):
    class Meta:
        model = ContactInfo
        exclude = {'user'}
        widgets = {
            'streetName': widgets.TextInput(attrs={'class': 'form-control'}),
            'houseNumber': widgets.TextInput(attrs={'class': 'form-control'}),
            'city': widgets.TextInput(attrs={'class': 'form-control'}),
            'country': widgets.TextInput(attrs={'class': 'form-control'}),
            'postCode': widgets.NumberInput(attrs={'class': 'form-control'}),
        }

class RatingForm(ModelForm):
    class Meta:
        model = Rating
        exclude = {'userBeingRated', 'userGivingRating', 'order'}
        widgets = {
            'rating': widgets.NumberInput(attrs={'class': 'form-control'}),
        }

