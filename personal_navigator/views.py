

from django.http import HttpResponse
from django.shortcuts import render


# Personal Navigator using templates


def index(request):
    return render(request, 'index.html')








