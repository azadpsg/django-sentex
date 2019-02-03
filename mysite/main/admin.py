from django.contrib import admin
from .models import Tutorial


class TutorialAdmin(admin.ModelAdmin):

    fieldsets = [
        ("Title / Date", {'fields': ["Tutorial_title", "Tutorial_published"]}),
        ("Content", {"fields": ["Tutorial_content"]})
    ]

admin.site.register(Tutorial,TutorialAdmin)