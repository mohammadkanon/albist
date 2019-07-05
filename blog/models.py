from django.db import models

# Create your models here.
class MainBlog(models.Model):
	blog_image = models.ImageField(upload_to='main-blog', null=True)
	blog_title = models.CharField(max_length=100, null=True)
	blog_details = models.TextField(max_length=300, null=True)