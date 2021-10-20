from django.shortcuts import render,HttpResponse,redirect
from django.template.loader import render_to_string
from django.core.mail import EmailMessage

from django.contrib.sites.shortcuts import get_current_site


def index(request):
    return render(request,'index.html')