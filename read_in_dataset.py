import glob
import cv2
import os

from ml_models.color_descriptor import *
from match.models import *

## Change to read in from config file
dataset_path = "%s/%s"%(os.getcwd(),'dataset/')

## Initialise ColorDescriptor
cd = ColorDescriptor((8, 12, 3))

## Loop through images, obtain features and store in DB
for imagePath in glob.glob(dataset_path + "/*.jpg"):
        ## Extract the image ID (i.e. the unique filename) from the image
        ## path and load the image itself
        imageID = imagePath[imagePath.rfind("/") + 1:]
        print('Image ID: ', imageID)

        img_id = int(imageID.replace(".jpg",''))
        
        image = cv2.imread(imagePath)
     
        ## Describe the image
        features = cd.describe(image)
        
        ## Save the features to db
        __image, created = Image.objects.update_or_create(
                                                        img_id=img_id,
                                                        defaults = {
                                                        "img_file": imagePath,
                                                        "img_features": features,
                                                        "img_type": "dataset",
                                                        },)
        if created:
            print(created)