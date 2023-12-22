from django.db import models
from django.utils import timezone

# Create your models here.
#DOC dos campos https://docs.djangoproject.com/pt-br/4.2/ref/models/fields/#field-choices

#nao esquecer de criar a migracao comando; python manage.py makemigrations
#nao esquecer de aplicar a migracao para ir pro BD; python manage.py migrate

class Category(models.Model):

    name = models.CharField(max_length=30)
        
    def __str__(self) -> str:
        return self.name


class Contact(models.Model):
    #campos obrigatorios / para nao ser obrigadorio acrescentar; blank=True no parametro
    first_name = models.CharField(max_length=12)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=11)
    email = models.EmailField(max_length=30, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    show = models.BooleanField (default=True)
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)

#colocando nome de exibicao dos contatos criados na lista a ser exibida
    
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
