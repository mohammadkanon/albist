from django.db import models

# Create your models here.
class BestServices(models.Model):
	best_service_title = models.CharField(max_length=20, null=True)
	best_service_details = models.TextField(max_length=200, null=True)

	def __str__(self):
		return self.best_service_title


class PlanFeaturs(models.Model):
	feature = models.TextField(null=True)

	def __str__(self):
		return self.feature

class UnlimitedPlan(models.Model):
	plan_name = models.CharField(max_length=50, null=True)
	plan_pay = models.IntegerField(null=True)
	plan_feature = models.ManyToManyField(PlanFeaturs)

	def __str__(self):
		return self.plan_name


class PremiumPlan(models.Model):
	plan_name = models.CharField(max_length=50, null=True)
	plan_pay = models.IntegerField(null=True)
	plan_feature = models.ManyToManyField(PlanFeaturs)

	def __str__(self):
		return self.plan_name


class AdvancePlan(models.Model):
	plan_name = models.CharField(max_length=50, null=True)
	plan_pay = models.IntegerField(null=True)
	plan_feature = models.ManyToManyField(PlanFeaturs)

	def __str__(self):
		return self.plan_name

class BasicPlan(models.Model):
	plan_name = models.CharField(max_length=50, null=True)
	plan_pay = models.IntegerField(null=True)
	plan_feature = models.ManyToManyField(PlanFeaturs)

	def __str__(self):
		return self.plan_name


		