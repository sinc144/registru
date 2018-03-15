from django import forms

from .models import Doc

class DocForm(forms.ModelForm):
    class Meta:
        model = Doc
        fields = [
            'title',
            'nrDoc',
            'dataDoc',
            'emitent',
            'beneficiar',
            'drumulNational',
            'partea',
            'drdp',
            'image',
            'rezolvat',
        ]