from django.forms import ModelForm, widgets
from users.models import Profile

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['id', 'user']
        widgets = {
            'first_name': widgets.TextInput(attrs={ 'class': 'form-control' }),
            'last_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'email': widgets.EmailInput(attrs={'class': 'form-control'}),
            'profile_image': widgets.TextInput(attrs={ 'class': 'form-control' })
        }