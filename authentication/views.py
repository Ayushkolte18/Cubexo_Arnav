from django.shortcuts import render,redirect
from authentication.forms import SignUpForm
from django.contrib.auth.decorators import login_required

from django.contrib.auth import login, authenticate
# Create your views here.


@login_required()
def Homepage(request):
    return render(request, 'registration/other.html')


