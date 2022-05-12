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
        'profile': get_object_or_404(Profile, pk=id)
    })

def profile(request):
    profile = Profile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = ProfileForm(instance=profile, data=request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            #return redirect('profile')
            return get_profile_by_id(request, Profile.user.id)
    return render(request, 'users/profile.html', {
        'form': ProfileForm(instance=profile)
    })