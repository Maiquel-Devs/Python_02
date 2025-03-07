from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['usuario', 'senha']
        widgets = {
            'senha': forms.PasswordInput()
        }
