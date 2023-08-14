from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
class Corses (models.Model):
    title=models.CharField(max_length=150)
    photo=models.ImageField(upload_to='photos/%Y/%m/%d')
    discribtion=models.TextField(max_length=200)
class Lectuer (models.Model):
    title=models.CharField(max_length=150)
    photo=models.ImageField(upload_to='photos/%Y/%m/%d')
    des=models.CharField(max_length=400)
    bdy=RichTextField(blank=True,null=True)
    cors_name=models.CharField(max_length=150)
    date=models.DateTimeField(default=datetime.now())
    def __str__(self):
        return self.title
