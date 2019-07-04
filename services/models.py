from django.db import models

# Create your models here.
class BestServices(models.Model):
	best_service_title = models.CharField(max_length=20, null=True)
	best_service_details = models.TextField(max_length=200, null=True)

	def __str__(self):
		return self.best_service_title

class Plan(models.Model):
	plan_name = models.CharField(max_length=50, null=True)

	def __str__(self):
		return self.plan_name

class PlanPay(models.Model):
	plan_pay = models.IntegerField(null=True)

	def __str__(self):
		return str(self.plan_pay)

class PlanFeaturs(models.Model):
	feature = models.TextField(null=True)

	def __str__(self):
		return self.feature

class PlanDetails(models.Model):
	plan = models.ForeignKey(Plan, on_delete= models.SET_NULL, null=True)
	planpay = models.ForeignKey(PlanPay, on_delete= models.SET_NULL, null=True)
	plan_feature = models.ManyToManyField(PlanFeaturs)

	def __str__(self):
		return str(self.plan)
		