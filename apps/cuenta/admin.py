from django.contrib import admin

# Register your models here.
from . import models
from django.contrib.auth import get_user_model

User = get_user_model()

class UserAdmin(admin.ModelAdmin):
    list_display = ('username','email','persona','es_activo', 'last_login', 'last_ip')
    list_display_links = ('username','email','persona')
    search_fields = ('username', 'email','es_activo','last_login')
    list_per_page = 25


admin.site.register(User,UserAdmin)