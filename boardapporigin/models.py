from django.db import models
from django.utils import timezone

class BoardModel(models.Model) :
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(upload_to = "media/",null=True,blank=True)
    good = models.IntegerField(null=True,blank=True,default=0)
    read = models.IntegerField(null=True,blank=True,default=0)
    read_text = models.CharField(max_length=50,null=True,blank=True,default="a")

    def __str__(self):
        return self.title+self.author+self.content

class Koushin(models.Model) :
    created_at = models.DateTimeField(default=timezone.now)

    
