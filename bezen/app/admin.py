from django.contrib import admin
from django.contrib.auth.models import Group
from app.models import recipe

# Register your models here.
admin.site.register(recipe)