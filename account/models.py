from django.db import models
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    phone = models.CharField(default="",max_length=30)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='./static/images')
    
    def __str__(self):
        return f'Profile for user {self.user.username}'
