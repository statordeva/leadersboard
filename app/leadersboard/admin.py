from django.contrib import admin

from .models import User, Winner

admin.site.register(User)
admin.site.register(Winner)