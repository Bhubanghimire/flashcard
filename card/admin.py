from django.contrib import admin
from card.models import Word


# Register your models here.
@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    list_display = ['id']
