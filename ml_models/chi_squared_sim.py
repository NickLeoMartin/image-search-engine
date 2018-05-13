# import the necessary packages
import numpy as np
import csv

class ChiSquaredSimilarity(object):
    """
    Uses Chi-Squared distance metric to calculate similarity on images stored in DB

    Example
    -------
    from match.models import Image
    from ml_models.chi_squared_sim import ChiSquaredSimilarity
    
    q = Image.objects.all()[0]
    images = Image.objects.all()[1:]
    sim_model = ChiSquaredSimilarity(q,images)
    topn = sim_model.obtain_similarity()
    
    """
    def __init__(self, query_image, images, limit=10):
        self.query_image = query_image
        self.images = images
        self.limit = limit

    def obtain_similarity(self):
        query_features = self.query_image.img_features
        results_dict = {}
        for img in self.images:
            features = [float(x) for x in img.img_features[1:]]
            d = self.chi2_distance(features, query_features)
            results_dict[img.id] = d
        return self.get_topn_similar_images(results_dict)

    def chi2_distance(self, histA, histB, eps = 1e-10):
        # compute the chi-squared distance
        d = 0.5 * np.sum([((a - b) ** 2) / (a + b + eps) for (a, b) in zip(histA, histB)])
        # return the chi-squared distance
        return d

    def get_topn_similar_images(self, results_dict):
        results = sorted([(v, k) for (k, v) in results_dict.items()])
        top_n_results = results[:self.limit]
        list_of_ids = [k for (v,k) in top_n_results]
        return list_of_ids 
