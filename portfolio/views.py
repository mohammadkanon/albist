from django.shortcuts import render
from portfolio.models import Blog

# Create your views here.
def portfolio(request):

	blog = Blog.objects.all()

	context = {
		'blog': blog
	}

	return render(request, 'portfolio/portfolio.html', context)