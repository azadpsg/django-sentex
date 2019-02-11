from django.contrib import admin
from .models import Tutorial, TutorialSeries, TutorialCategory


class TutorialAdmin(admin.ModelAdmin):

    fieldsets = [
        ("Title / Date", {'fields': ["Tutorial_title", "Tutorial_published"]}),
        ("Content", {"fields": ["Tutorial_content"]}),
        ("Series", {'fields': ["Tutorial_series"]}),
        ("URL", {'fields': ["Tutorial_slug"]}),
    ]


admin.site.register(Tutorial,TutorialAdmin)
admin.site.register(TutorialSeries)
admin.site.register(TutorialCategory)
