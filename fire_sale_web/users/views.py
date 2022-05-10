from django.shortcuts import render, redirect
from forms.profile_form import ProfileForm
from users.models import User, Profile
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def index(request):
    return render(request, 'users/index.html', {
        'users': User.objects.all()
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

def profile(request):
    profile = Profile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = ProfileForm(instance=profile, data=request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile')
    return render(request, 'users/profile.html', {
        'form': ProfileForm(instance=profile)
    })