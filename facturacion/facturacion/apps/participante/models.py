from django.db import models

# Create your models here.
class Participante(models.Model):
    username = models.CharField(max_length=30, unique=False)
    password = models.CharField(max_length=60, unique=False)
    
    def __unicode__(self):
        return self.username
        
    class Meta:
        unique_together = ("username", "password")
        
    