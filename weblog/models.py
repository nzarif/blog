from django.db import models

# Create your models here.
class Weblog(models.Model):
    title= models.CharField(max_length=200, unique=True)
    image = models.TextField(max_length=10000 , blank=True , null=True )
    author = models.CharField(foreign_key=User.username)
    description = models.TextField(max_length=25000000 , blank=True , null=True )

class Post(models.Model):
    text=models.TextField()
    title=models.CharField(max_length=25)
    summary=models.TextField(max_length=300)
    id=models.CharField(max_length=10 , primary_key=True)
    weblog=models.CharField(foreign_key=Weblog.title)

class User(models.Model):
    username=models.CharField(primary_key=True,max_length=25)
    password=models.CharField(max_length=12)
    firstName=models.CharField(max_length=25)
    lastName=models.CharField(max_length=25)
    email=models.CharField(max_length=50)

class Comment(models.Model):
    postId=models.CharField(max_length=10, foreign_key=Post.id)
    text=models.TextField()
    id=models.CharField(primary_key=True)
    user=models.CharField(foreign_key=User.username)
