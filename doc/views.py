# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

from .forms import DocForm
from .models import Doc

# Create your views here.
def doc_registru(request):
    queryset = Doc.objects.all()
    context = {
        'object_list': queryset,
        'title': 'Registru'
    }
    return render(request, "registru.html", context)

def doc_home(request):
    context = {
        'title': 'Home'
    }
    return render(request, "doc_home.html", context)

def doc_about(request):
    context = {
        'title': 'About'
    }
    return render(request, "about.html", context)

def doc_contact(request):
    context = {
        'title': 'Contact'
    }
    return render(request, "contact.html", context)

def doc_detail(request):
    context = {
        'title': 'Detail'
    }
    return render(request, "doc_detail.html", context)

def doc_create(request):
    form = DocForm(request.POST or None, request.FILES or None)
    context = {
        'form': form
    }
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request,'Succesfully created')
        return HttpResponseRedirect(instance.get_absolut_url())

    return render(request, "doc_create.html", context)

def doc_update(request):
    context = {
        'title': 'Update'
    }
    return render(request, "doc_update.html", context)

def doc_delete(request):
    context = {
        'title': 'Delete'
    }
    return render(request, "doc_delete.html", context)