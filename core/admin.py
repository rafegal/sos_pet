from django.contrib import admin
from .models import Pet

# Register your models here.

#admin.site.register(PetLost)
@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ['id', 'city', 'user', 'active',]
    search_fields = ['id', 'user__username']


