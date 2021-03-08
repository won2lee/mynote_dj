from django.contrib import admin

# Register your models here.

from .models import Note, First_Category, Second_Category

admin.site.register(Note)

admin.site.register(First_Category)
admin.site.register(Second_Category)