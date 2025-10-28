
from django import forms
from .models import Livro, Autor, Genero

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['titulo', 'autores', 'generos']
