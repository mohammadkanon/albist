from django.contrib import admin
from services.models import BestServices, PlanFeaturs, UnlimitedPlan, PremiumPlan, AdvancePlan, BasicPlan

# Register your models here.
admin.site.register(BestServices)
admin.site.register([PlanFeaturs, UnlimitedPlan, PremiumPlan, AdvancePlan, BasicPlan])