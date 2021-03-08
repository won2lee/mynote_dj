from django.db import models
from django.urls import reverse

# Create your models here.


class First_Category(models.Model):
	first_cat = models.CharField(max_length=100)

	def __str__(self):
		return f'{self.first_cat}'


class Second_Category(models.Model):	
	first_cat = models.ForeignKey('First_Category', on_delete=models.SET_NULL, null=True)
	second_cat = models.CharField(max_length=100, blank=True, null=True)

	def __str__(self):
		return f'{self.second_cat}'

class Note(models.Model):
	first_cat = models.ForeignKey('First_Category', on_delete=models.SET_NULL, null=True)
	second_cat = models.ForeignKey('Second_Category', on_delete=models.SET_NULL, null=True)
	memo = models.TextField(max_length=1000, help_text='Enter your memo')
	created = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f'{self.first_cat}/{self.second_cat}:{str(self.created)[:10]} [{self.id}]'

	def get_absolute_url(self):
		"""Returns the url to access a detail record for this book."""
		return reverse('note-detail', args=[str(self.id)])


