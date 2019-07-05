from django.urls import path
from pages.views import pages

urlpatterns = [
    path('', pages, name='pages')
]