from django.shortcuts import render
from django.views.generic.list import ListView

from random import sample

from .models import Image
from ml_models.chi_squared_sim import ChiSquaredSimilarity


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


class SearchResultsView(ListView):
	template_name = "match/02_search_results.html"
	context_object_name = "similar_images"

	def get_queryset(self, **kwargs):
		## Get all other images
		images = Image.objects.exclude(id__in=self.kwargs['q_id'])

		## Get qurey image
		q = Image.objects.get(id=self.kwargs['q_id'])

		## Get ids for most similar images
		sim_model = ChiSquaredSimilarity(q,images)
		topn_ids = sim_model.obtain_similarity()

		## Filter by topn_ids
		similar_images = Image.objects.filter(id__in=topn_ids)

		## Return images
		return similar_images


