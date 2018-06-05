from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.core.urlresolvers import resolve
import datetime
import re
from .models import *

# Create your views here.
def main_page(request):
    print(request)
    return render(request, 'menu/main_page.html', {'path': request.path})


