from django.db import models
from django.contrib.auth.models import User

"""
class User(models.Model):
    
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=15)

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)

    bio = models.TextField(blank=True)
    
    birthdate = models.DateField(blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    
    country = models.CharField(max_length=50,blank=True,null=True,default="")
    city = models.CharField(max_length=50,blank=True,null=True,default="")

    def __str__(self):
        return "{name} | {email} | Cumpleaños: {birthdate} | Ingreso: {created} | Es Admin: {is_admin}".format(
                    name = self.first_name + ' ' + self.last_name,
                    email = self.email,
					birthdate = self.birthdate,
					created = self.created,
					is_admin = self.is_admin
                    )
"""

class Post(models.Model):
    """Post model."""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #Evita referencias circular con el String
    profile = models.ForeignKey('users.Profile', on_delete=models.CASCADE)

    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='posts/photos')

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return title and username."""
        return '{} by @{}'.format(self.title, self.user.username)
