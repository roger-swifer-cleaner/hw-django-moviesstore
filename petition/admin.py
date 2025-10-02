from django.contrib import admin
from .models import Petition

class PetitionAdmin(admin.ModelAdmin):
    ordering = ['name']
    search_fields = ['name']

admin.site.register(Petition)
