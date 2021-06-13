from django.shortcuts import render
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.shortcuts import redirect
from django.dispatch import receiver
from . import models


def works(request):
    projects = models.Project.objects.all()
    return render(request, 'works/works.html', {'projects': projects})

def form_send(request):
    if request.method == 'POST': #метод протокола http
        name = request.POST['name']
        surname = request.POST['surname']
        description = request.POST['description']
        email = request.POST['email']
        number = request.POST['number']
        a = models.Form()
        a.name = name
        a.surname = surname
        a.description = description
        a.email = email
        a.number = number
        if a.description!='':
            if a.number!='':
                a.save()
    return redirect ('works')
	