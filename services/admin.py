from django.contrib import admin
from services.models import BestServices, Plan, PlanPay, PlanFeaturs, PlanDetails

# Register your models here.
admin.site.register(BestServices)
admin.site.register([Plan, PlanPay, PlanFeaturs, PlanDetails])