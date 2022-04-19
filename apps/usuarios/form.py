from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

class UsuarioForm(UserCreationForm):
    email = forms.EmailField(max_length=100)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def clean_email(self):
        e = self.cleaned_data['email']
        if User.objects.filter(email=e).exists():
            raise ValidationError("O e-mail {} já está em uso.".format(e))

        return e

    def clean_username(self):
        e = self.cleaned_data['username']
        if User.objects.filter(username=e).exists():
            raise ValidationError("O nome de usuário {} já está em uso.".format(e))

        return e