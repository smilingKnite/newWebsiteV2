from __future__ import unicode_literals

import re
import sys

from django.contrib import messages
from django.shortcuts import redirect, render

import bcrypt
from models import *

#################################################################################################


def index(request):
    # users = Users.objects.all()

    return render(request, 'webPortfolio/index.html')


#################################################################################################


def photos(request):
    # users = Users.objects.all()

    return render(request, 'webPortfolio/photos.html')


#################################################################################################


def designs(request):
    # users = Users.objects.all()

    return render(request, 'webPortfolio/designs.html')


#################################################################################################


def me(request):
    # users = Users.objects.all()

    return render(request, 'webPortfolio/resume.html')


#################################################################################################


def work(request):
    # users = Users.objects.all()

    return render(request, 'webPortfolio/work.html')


#################################################################################################

# def signIn(request):
#     errors = Users.objects.verify(request.POST)
#     if len(errors):
#         for tag, error in errors.iteritems():
#             messages.error(request, error, extra_tags=tag)
#         return redirect('/')
#     else:
#         # request.session['name'] = request.POST['name']
#         request.session['email'] = request.POST['email']
#         context = {
#             # 'name': request.session['name'],
#             'email': request.session['email'],
#             'user': Users.objects.all(),
#             'thing': Stuff.objects.all()
#         }
#         return redirect('/dash', context)
