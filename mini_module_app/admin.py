from django.contrib import admin
from .models import Files, Calendar

class FileAdmin(admin.ModelAdmin):
    list_display = ['title', 'subject', 'type']
    search_fields = ['title', 'subject', 'type']
    list_filter = ['subject', 'type']


admin.site.register(Files, FileAdmin)
admin.site.register(Calendar)
