from datetime import date

from django import forms

from acceso.models import Usuario
from core.models import Book

import re


class BookForm(forms.ModelForm):

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) < 1:
            raise forms.ValidationError(
                'Titulo debe tener minimo 2 caracteres ')
        return title

    def clean_description(self):
        description = self.cleaned_data['description']
        if len(description) < 5:
            raise forms.ValidationError(
                'Titulo debe tener minimo 5 caracteres ')
        return description

    class Meta:
        model = Book
        fields = ['title', 'description']

        labels = {
            'title': 'Título: ',
            'description': 'Descripción: '
        }

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }
