from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
from . import forms, models

class MyUserAdmin(UserAdmin):
    add_form = forms.MyUserCreationForm
    form = forms.MyUserChangeForm
    model = models.User
    list_display = ['username', 'email', 'fullname', 'phone']

admin.site.register(models.User, MyUserAdmin)
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Category)
admin.site.register(Book)
admin.site.register(BookRent)
