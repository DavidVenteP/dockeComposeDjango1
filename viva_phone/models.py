from django.db import models

# Create your models here.

class feature_item(models.Model):
	"""
		Description
			Store the app features.
	"""
	icon = models.CharField(verbose_name='Icono', max_length = 200)
	title = models.CharField(verbose_name='Título', max_length = 50)
	description = models.CharField(verbose_name='Descripción', max_length = 300)
    