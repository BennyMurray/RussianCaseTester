from django.contrib import admin
from .models import Word

class WordAdmin(admin.ModelAdmin):
    list_display = Word._meta.get_all_field_names()

admin.site.register(Word, WordAdmin)
