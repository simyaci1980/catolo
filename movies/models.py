from django.db import models

# Create your models here.


class Movie (models.Model):
	name= models.CharField(max_length=100 , verbose_name= 'FİLM ADI ')
	description = models.TextField( verbose_name='FİLM AÇIKLAMASI ')
	image= models.CharField(max_length=50  , verbose_name='FİLM RESMİ ')
	created_date= models.DateTimeField(auto_now_add=True  , verbose_name='EKLEME TARİHİ ')
	isPublished=models.BooleanField(default=True )
	search_fields=('name', 'description')
	

	def __str__(self) :
		return self.name
		
	def get_image_path(self):
		return '/img/' +  self.image	