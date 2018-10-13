from django.db import models

class Fruits(models.Model):
    name=models.CharField(max_length=20)
    origin=models.TextField()
    scientific_name=models.TextField(null=True)
    rank=models.CharField(max_length=20,null=True)
    hybrid=models.TextField(null=True)
    cultivar=models.CharField(max_length=30,null=True)
    text=models.TextField()
    telugu=models.TextField(null=True)

class Uploads(models.Model):
    image=models.ImageField(upload_to='images')
    name=models.CharField(max_length=20,null=True)

class Diseases(models.Model):
    name=models.CharField(max_length=20)
    symptoms=models.TextField()
    desc=models.TextField()
    sol=models.TextField()