from django.db import models

# Create your models here.
class TopSlider(models.Model):
	slider_img = models.ImageField(upload_to='topslider', null=True, default='default.jpg')

class OurServices(models.Model):
	service_title = models.CharField(max_length=50, null=True)
	service_detail = models.TextField(max_length=300, null=True)

class ImageGallery(models.Model):
	gallery = models.ImageField(upload_to='imagegallery', null=True)

class EmployeGallery(models.Model):
	emp_name = models.CharField(max_length=100, null=True)
	emp_position = models.CharField(max_length=150, null=True)
	emp_photo = models.ImageField(upload_to='mengallery', null=True)

class FeatersColumn(models.Model):
	feater_title = models.CharField(max_length=50, null=True)
	feater_dep1 = models.CharField(max_length=100, null=True)
	feater_dep2 = models.CharField(max_length=100, null=True)
	feater_dep3 = models.CharField(max_length=100, null=True)
	feater_dep4 = models.CharField(max_length=100, null=True)
