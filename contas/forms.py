from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CadastroUsuarioForm(UserCreationForm):
    
    primeiro_nome = forms.CharField('Primeiro Nome', max_length=50, required=True, help_text='Campo de nome obrigatório' )
    ultimo_nome = forms.CharField('Ultimo Nome', max_length=50, required=True, help_text='Campo de nome obrigatório')
    email = form.EmailField('E-mail', max_length=250, help_text='Por favor insira um e-mail válido')

    class Meta: 
        model = User
        fields = ['username', 
            'username',
            'primeiro_nome',
            'ultimo_nome',
            'email',
            'password1'
            'password2'
        
        
        
        ]

