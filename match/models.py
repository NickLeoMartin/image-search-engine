from django.db import models
from picklefield.fields import PickledObjectField
import datetime
import json


IMAGECHOICES = (('dataset', 'dataset'),('uploaded','uploaded'))

class Image(models.Model):
	""" Model to store path to images and features """
	img_id = models.IntegerField(default=-1)
	img_file = models.ImageField(upload_to="img")
	img_features = PickledObjectField(default=None)
	img_type = models.CharField(max_length=100,default='dataset',choices=IMAGECHOICES)

	def __str__(self):
	    return "%s - %s"%(self.img_type,self.img_file.name)


class MostSimilarImages(models.Model):
	""" Storage for most similar images list of pks """
	sim_uploaded_image = models.ForeignKey(Image,related_name='img_most_sim',on_delete=models.CASCADE,null=True,blank=True)
	sim_top_n = PickledObjectField(default='') ##list of ordered pks
	sim_algo = models.CharField(max_length=100,default='')

	def __str__(self):
		return "%s - %s"%(self.sim_algo,self.sim_uploaded_image)