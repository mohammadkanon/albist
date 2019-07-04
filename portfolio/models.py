from django.db import models

# Create your models here.
class Blog(models.Model):
	blog_img = models.ImageField(upload_to='blog', null=True)
	blog_title = models.CharField(max_length=50, null=True)
	blog_details = models.TextField(max_length=300, null=True)
