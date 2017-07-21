from django.db import models
from authc.models import User



class Weblog(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200, unique=True)
    image = models.TextField(max_length=10000 , blank=True, null=True )
    author = models.ForeignKey(User)
    description = models.TextField(max_length=25000000 , blank=True , null=True)
    pass


class Post(models.Model):
    text=models.TextField()
    title=models.CharField(max_length=25)
    summary=models.TextField(max_length=300)
    id=models.CharField(max_length=10 , primary_key=True)
    weblog=models.ForeignKey(Weblog)
    date=models.TimeField()
    pass


class Comment(models.Model):
    pid=models.ForeignKey(Post,default=None)
    text=models.TextField()
    id=models.IntegerField(primary_key=True)
    date = models.DateField(default=None)