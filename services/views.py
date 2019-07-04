from django.shortcuts import render
from index.models import FeatersColumn
from services.models import BestServices, PlanDetails, PlanFeaturs

# Create your views here.
def services(request):
	best_service = BestServices.objects.all()
	feater = FeatersColumn.objects.all()
	plans = PlanDetails.objects.all()
	featurs = PlanFeaturs.objects.all()

	context = {
		'best_service': best_service,
		'feater': feater,
		'plans': plans,
		'featurs': featurs,
	}
	return render(request, 'services/services.html', context)