from django.contrib import admin
from .models import Website

# Register your models here.



class keywordAdmin(admin.ModelAdmin):
    list_display  = ('website', 'temp_keywords')

admin.site.register(Website, keywordAdmin)