from django.shortcuts import render, redirect
from users.models import User
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