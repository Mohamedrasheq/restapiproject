from django.db import models

# Create your models here.

class BlogPost(models.Model):
    title=models.CharField(max_length=500)
    content=models.TextField()
    published_date=models.DateTimeField(auto_now_add=True)
