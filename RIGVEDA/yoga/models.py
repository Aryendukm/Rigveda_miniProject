from django.db import models

# Create your models here.
class ans(models.Model):
    name1 = models.CharField(max_length=300)
    name2=models.CharField(max_length=300)
    name3=models.CharField(max_length=300)
    picture1 = models.ImageField(upload_to='yogaimg')
    picture2 = models.ImageField(upload_to='yogaimg')
    picture3 = models.ImageField(upload_to='yogaimg')
    problem = models.CharField(max_length=500)
    description = models.TextField()

    def __str__(self):
        return self.problem




class userinfo(models.Model):
    username = models.CharField(max_length=80)
    email = models.EmailField()
    password = models.CharField(max_length=16)
    problem = models.CharField(max_length=50)

    def __str__(self):
        return self.username
