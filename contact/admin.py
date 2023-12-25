from django.contrib import admin
from contact import models

# Register your models here.
@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id','first_name','last_name','phone','show'
    ordering = '-id',
    search_fields = 'first_name','last_name',
    list_per_page = 10 #itens por pagina
    list_max_show_all = 20
    list_editable = 'first_name', 'last_name', 'show',
    #filtros
    # list_filter = 'created_date',

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'name',
    ordering = '-id',