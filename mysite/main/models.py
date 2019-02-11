from django.db import models
from datetime import datetime

class TutorialCategory(models.Model):
	category = models.CharField(max_length=200)
	summery = models.CharField(max_length=200)
	slug = models.CharField(max_length=200, default=1)
	class Meta:
		#name for admin page
		verbose_name_plural = "Categories"

	def __str__(self):
		return self.category

class TutorialSeries(models.Model):
	tutorial_series = models.CharField(max_length=200)

	category = models.ForeignKey(TutorialCategory, default=1, verbose_name="Category", on_delete=models.SET_DEFAULT)
	series_summary = models.CharField(max_length=200)

	class Meta:
		# otherwise we get "Tutorial Seriess in admin"
		verbose_name_plural = "Series"

	def __str__(self):
		return self.tutorial_series

class Tutorial(models.Model):
	Tutorial_title = models.CharField(max_length=200)
	Tutorial_content = models.TextField()
	Tutorial_published = models.DateTimeField("date published")
	Tutorial_edit = models.DateTimeField("Date Edited", default=datetime.now )
	Tutorial_series = models.ForeignKey(TutorialSeries, default=1, verbose_name="Series", on_delete=models.SET_DEFAULT)
	Tutorial_slug = models.CharField(max_length=200, default=1)
	def __str__(self):
		return self.Tutorial_title
