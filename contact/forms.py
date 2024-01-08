from django import forms
from django.core.exceptions import ValidationError
from . import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class ContactForm(forms.ModelForm):
    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
            'accept': 'image/*',
            }
        )
    )

    class Meta:
        model = models.Contact
        fields = ('first_name','last_name', 'phone', 'email', 'description', 'category', 'picture',)
        # widget=forms.TextInput(
        #     attrs={
        #         'class': 'classe-a classe b',
        #         'placeholder': 'Aqui veio do init',
        #     }
        # )
    
    def clean(self):
        cleaned_data = self.cleaned_data
        first_name =cleaned_data.get('first_name')
        last_name =cleaned_data.get('last_name')

        if first_name == last_name:
            msg = ValidationError('Segundo nome nao pode ser igual ao primeiro', code='invalid')
            self.add_error('first_name', msg)
            self.add_error('last_name', msg)

        #self.add_error('first_name', ValidationError('Mensagem do erro', code='invalid'))

        return super().clean()
    
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')

        if first_name == 'ABC':
            self.add_error(
            'first_name', ValidationError('retorn o valor do campo aqui', code='invalid'))
        print('TESTE')
        
        return first_name
    
class RegisterForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    lasT_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email', 'username', 'password1','password2',
        )
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            self.add_error('email',
                           ValidationError('Ja existe esse email', code='invalid'))

        return email