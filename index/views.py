from django.shortcuts import render
from index.models import TopSlider, OurServices, ImageGallery, EmployeGallery, FeatersColumn

# Create your views here.
def home(request):
	slider = TopSlider.objects.all()
	services = OurServices.objects.all()
	gallery = ImageGallery.objects.all()
	employe = EmployeGallery.objects.all()
	feater = FeatersColumn.objects.all()

	context = {
		'slider': slider,
		'services': services,
		'gallery': gallery,
		'employe': employe,
		'feater': feater,

	}

	return render(request, 'index/home.html', context)


def about(request):
	return render(request, 'index/about.html')