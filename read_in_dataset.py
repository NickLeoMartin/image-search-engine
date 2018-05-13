import glob
import cv2
import os

from ml_models.color_descriptor import *
from match.models import *

## Change to read in from config file
media_path = "%s/%s"%(os.getcwd(),'media/img/')

## Initialise ColorDescriptor
cd = ColorDescriptor((8, 12, 3))

## Loop through images, obtain features and store in DB
for image_path in glob.glob(media_path + "/*.jpg"):
        ## Extract the image ID (i.e. the unique filename) from the image
        ## path and load the image itself
        imageID = image_path[image_path.rfind("/") + 1:]
        print('Image ID: ', imageID)

        img_id = int(imageID.replace(".jpg",''))
        
        image = cv2.imread(image_path)
     
        ## Describe the image
        features = cd.describe(image)
        
        ## Media path
        full_image_path = os.path.join('img',imageID)
        print(image_path)
        print(full_image_path)

        ## Save the features to db
        __image, created = Image.objects.update_or_create(
                                                        img_id=img_id,
                                                        defaults = {
                                                        "img_file": full_image_path,
                                                        "img_features": features,
                                                        "img_type": "dataset",
                                                        },)
        if created:
            print(created)