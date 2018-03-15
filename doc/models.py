# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.forms import ModelForm
from django.core.urlresolvers import reverse

# Create your models here.
STATUS_CHOICES = (
    ('Dreapta', 'Dreapta'),
    ('Stanga', 'Stanga'),
)

STATUS_CHOICES_DRDP = (
    ('Bucuresti', 'Bucuresti'),
    ('Craiova', 'Craiova'),
    ('Timisoara', 'Timisoara'),
    ('Cluj', 'Cluj'),
    ('Brasov', 'Brasov'),
    ('Iasi', 'Iasi'),
    ('Constanta', 'Constanta'),
)

def upload_location(instance, filename):
    return '%s/%s' %(instance.id, filename)


class Doc(models.Model):
    title               = models.TextField()
    image               = models.FileField(upload_to=upload_location, null=True, blank=True)    
    nrDoc               = models.IntegerField()
    dataDoc             = models.DateField()
    emitent             = models.CharField(max_length=100)
    beneficiar          = models.CharField(max_length=100)
    drumulNational      = models.CharField(max_length=10)
    pozitiaKilometrica  = models.CharField(max_length=50)
    partea              = models.CharField(max_length=7, null=True, blank=True,choices=STATUS_CHOICES)
    drdp                = models.CharField(max_length=10, null=True, blank=True,choices=STATUS_CHOICES_DRDP)
    creat               = models.DateTimeField(auto_now=False, auto_now_add=True)
    modificat           = models.DateTimeField(auto_now=True, auto_now_add=False)
    rezolvat            = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolut_url(self):
        return reverse("doc:detalii", kwargs={'id': self.id})
        #return "/document/%s/" %(self.id)

    class Meta:
        ordering = ['-creat', '-modificat']