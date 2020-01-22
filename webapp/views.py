from django.shortcuts import render
from django.core import serializers

from .Database import records, records1
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from .serializers import Myserializers


# Create your views here.

def daily_database(request):
    return render(request, 'Myhtml/Database.html', {"records": records1})


def master_database(request):
    return render(request, 'Myhtml/Database.html', {"records": records})



