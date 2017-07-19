from django.db import models


class User(models.Model):
    username = models.CharField(primary_key=True,max_length=25)
    password = models.CharField(max_length=12)
    firstName = models.CharField(max_length=25)
    lastName = models.CharField(max_length=25)
    email = models.CharField(max_length=50)
    bid = models.IntegerField()
    pass


class Weblog(models.Model):
    bid = models.IntegerField()
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
    pass


class Comment(models.Model):
    postId=models.ForeignKey(Post)
    text=models.TextField()
    id=models.CharField(primary_key=True)
    user=models.ForeignKey(User)