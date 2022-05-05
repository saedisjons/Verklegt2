from django.shortcuts import render
from users.models import User

# Create your views here.
def index(request):
    return render(request, 'users/index.html', {
        'users': User.objects.all()
    })