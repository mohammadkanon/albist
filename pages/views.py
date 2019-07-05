from django.shortcuts import render
from index.models import OurServices
from services.models import BestServices, PlanDetails, PlanFeaturs

# Create your views here.
def pages(request):
	best_service = BestServices.objects.all()
	services = OurServices.objects.all()
	plans = PlanDetails.objects.all()
	featurs = PlanFeaturs.objects.all()

	context = {
		'best_service': best_service,
		'services': services,
		'plans': plans,
		'featurs': featurs,
	}


	return render(request, 'pages/pages.html', context)
