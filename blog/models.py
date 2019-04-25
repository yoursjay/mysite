from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Blog(models.Model):
    title = models.CharField(verbose_name='标题',max_length=50)
    content = models.TextField()
    image = models.ImageField(default='default.jpg',upload_to='images/')
    author = models.ForeignKey(User,on_delete=models.DO_NOTHING,verbose_name='作者')
    created_time = models.DateTimeField(verbose_name='创建日期',auto_now_add=True)
    last_updated_time = models.DateTimeField(verbose_name='更新日期',auto_now=True)