from django.db import models

# Create your models here.


class Gallery(models.Model):
    description = models.CharField(default='在这里输入作品的简介',max_length=100)
    tittle = models.CharField(default='作品标题',max_length=100)
    image = models.ImageField(default='default.jpg',upload_to='images/')
    ordering = ['id']
    
    def __str__(self):
        """Unicode representation of MODELNAME."""
        return self.tittle

