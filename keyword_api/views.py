from django.shortcuts import render
from django.shortcuts import get_object_or_404
# Create your views here.
from .models import Website
import json
from django.http.response import JsonResponse


def keywords(request):
    pk = request.GET.get('pk')
    site = get_object_or_404(Website, pk=pk)
    return JsonResponse(site.keywords, status=200, safe=False)
