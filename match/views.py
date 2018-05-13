from django.shortcuts import render
from django.views.generic.list import ListView

from random import sample

from .models import Image

# Create your views here.

class IndexView(ListView): 
	# model = Image
	template_name = 'match/01_index.html'
	context_object_name = "images"

	def get_queryset(self):
		""" Randomly sample k images """
		k = 5
		sampled_ids = sample(list(Image.objects.all().values_list('id',flat=True)),k)
		sampled_images = Image.objects.filter(id__in=sampled_ids)
		return sampled_images
