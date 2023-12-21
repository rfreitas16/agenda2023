from django.contrib import admin
from contact import models

# Register your models here.
@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id','first_name','last_name','phone',
    ordering = '-id',
    search_fields = 'first_name','last_name',
    list_per_page = 1 
    list_max_show_all = 20
    # list_editable = 'first_name', 'last_name',


    #filtros
    # list_filter = 'created_date',