from django.db import models
from django.contrib.auth.models import User


# Model para Avatares
class Avatar(models.Model):
    user = models.OneToOneField (User, on_delete=models.CASCADE, null=True, blank=True)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)
    def __str__(self):
        return f"{self.user} - {self.imagen}"
    
