from django.db import models

# Create your models here.

class Image(models.Model):
    i_1=models.ImageField(upload_to='pic')
    name=models.CharField(max_length=100,default='pandi')


    @property
    def imageurl(self):
        try:
            url=self.i_1.url
        except:
            url=""
        return url
