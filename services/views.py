from django.shortcuts import render
from index.models import FeatersColumn
from services.models import BestServices, UnlimitedPlan, PremiumPlan, AdvancePlan, BasicPlan

# Create your views here.
def services(request):
	best_service = BestServices.objects.all()
	unlimited_plan = UnlimitedPlan.objects.all()
	premium_plan = PremiumPlan.objects.all()
	advance_plan = AdvancePlan.objects.all()
	basic_plan = BasicPlan.objects.all()

	context = {
		'best_service': best_service,
		'unlimited_plan': unlimited_plan,
		'premium_plan': premium_plan,
		'advance_plan': advance_plan,
		'basic_plan': basic_plan
	}
	return render(request, 'services/services.html', context)