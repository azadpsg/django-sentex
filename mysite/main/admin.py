from django.contrib import admin
from .models import Tutorial

class TutorialAdmin(admin.ModelAdmin):
	#fields = ['Tutorial_title',
	#		  'Tutorial_published',
	#		  'Tutorial_content',
	#			]
	fieldset = [
			("Title/date", {'fields': ["Tutorial_title", "Tutorial_published"]}),
			("Content", { 'fields': [ "Tutorial_content"]})

			]

admin.site.register(Tutorial, TutorialAdmin)

