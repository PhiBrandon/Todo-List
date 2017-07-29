from django.db import models

# Create your models here.
class TodoList(models.Model):
	title 		= models.CharField(max_length=200)
	started 	= models.DateTimeField(auto_now_add=True)
	completed 	= models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title