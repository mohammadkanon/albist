from django.shortcuts import render
from blog.models import MainBlog

# Create your views here.
def blog(request):
	mblog = MainBlog.objects.all()

	context = {
		'mblog': mblog
	}

	return render(request, 'blog/blog.html', context)
