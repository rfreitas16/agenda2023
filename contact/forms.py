from django import forms
from django.core.exceptions import ValidationError
from . import models

class ContactForm(forms.ModelForm):
    class Meta:
        model = models.Contact
        fields = ('first_name','last_name',)
    
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