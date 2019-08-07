from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
	
	user = models.OneToOneField(User, on_delete = models.CASCADE)

	website = models.URLField(max_length=200, blank=True)
	biography = models.TextField(blank=True)
	phone_number = models.CharField(max_length=20, blank=True)

	create = models.DateTimeField(auto_now_add = True)
	modified = models.DateTimeField(auto_now = True)
	
	# Media - Requiere la instalación de Pillow

	picture = models.ImageField(upload_to = 'users/pictures', blank = True, null = True)
	
	def __str__(self):
		return self.user.username
	
