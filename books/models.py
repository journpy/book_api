from django.db import models


class Author(models.Model):
	"""An author"""
	prefix = models.CharField(max_length=20, blank=True, null=True)
	name = models.CharField(max_length=100, blank=True)

	def __str__(self):
		return f'{self.prefix} {self.name}'


class Book(models.Model):
	"""A book."""
	title = models.CharField(max_length=100)
	subtitle = models.CharField(max_length=250)
	author = models.ForeignKey(
		Author, 
		on_delete=models.CASCADE, 
		related_name='books'
		)
	isbn = models.CharField(max_length=13)
	
	def __str__(self):
		return f'Title: {self.title} Subtitle: {self.subtitle}'


