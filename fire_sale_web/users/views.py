from django.shortcuts import render, redirect, get_object_or_404
from users.forms.profile_form import ProfileForm
from users.models import User, Profile
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def index(request):
    return render(request, 'users/index.html', {
        'users': Profile.objects.all()
    })

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'users/register.html', {
        'form': UserCreationForm()
    })

#/items/3
def get_profile_by_id(request, id):
    return render(request, 'users/profile.html', {
        'user_profile': get_object_or_404(User, pk=id),
        'profile': get_object_or_404(Profile, user_id = id)
    })

def update_profile(request, id):
    profile = Profile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = ProfileForm(instance=profile, data=request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            request.user.email = form.cleaned_data.get('email')
            request.user.first_name = form.cleaned_data.get('first_name')
            request.user.last_name = form.cleaned_data.get('last_name')
            request.user.profile_image = form.cleaned_data.get('profile_image')
            request.user.save()
            profile.save()
            return get_profile_by_id(request, profile.user_id)
    return render(request, 'users/update_profile.html', {
        'form': ProfileForm(instance=profile),
        'profile': profile,
        'id': id
    })
