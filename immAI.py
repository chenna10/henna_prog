'''
Created on Jun 1, 2017

@author: che
'''
from clarifai.rest import ClarifaiApp
from clarifai.rest import  Image as ClImage
from glob import glob
import os
#This is the main class for the AI program within this class you will create your application from your app ID and your app Secret, you will upload your image sets to the
#subfunction titled "create_image_set" which will do a bulk import for all the iamges you want loaded into you app. From there you will create a model for the app.
#When creating the model make sure the Model Id is a descriptive name for the product group you are going to be working with. You will also create your concepts. As of now the
#concepts are the meta data (keywords) for the images with in IMM. You will then train the model with the model.train() object. Once the model has been trained you will have 
#the object app.models.get() grab your model based on the name you created earlier. The program will then out put a prompt asking you to input the url for the image you
#you want to be tagged. The application will then read the url based on the image within and bitmap whether or not this is a good match. If the output for the data is less then 
#95% discuss with someone on whether or not you have chosen a valid image match. All of this must be done through the clarifai.com. 

#When you go on clarifai.com you will need to ask for permission to the developers api if it is granted you will receive your client ID and client Secret. 
#There are tutorials on how to install this software to your computer, but you must make sure that you have installed Python 2.7 and created a path in your directory
#so that you can write on the command line windows prompt: python -m pip install clarifai. Once the software is installed follow the directions I stated above. 
#This is a link that will bring you through the process of doing the actually upload of images and image tagging: "http://blog.clarifai.com/train-a-custom-visual-recognition-model-using-clarifais-python-client/#.WSRIPmgrLRY" 
def main():
    app = ClarifaiApp('hhv0uGpoC__5f32QzxEOgZoxSBPHacQhzXTkhu29', 'ngwfVvM00U2SKU-_krMaooHvRY2ew03T_oOFmlsb')
    #image_set1 = create_image_set('C:\Python27\Projects\Outlets and Faceplates', concepts=['Product. Outlets and Faceplates single channel double channel. White'])
    #image_set2 = create_image_set('C:\Python27\Projects\Group Outlets and Faceplates', concepts=['Group. Outlets and Faceplates single channel double channel. White'])
    #app.inputs.bulk_create_images(image_set1)
    #app.inputs.bulk_create_images(image_set2)
    
    #model = app.models.create(model_id="Outlets and Faceplates", concepts=['Product. Outlets and Faceplates single channel double channel. White', "Group. Outlets and Faceplates single channel double channel. White"])
    #model.train()
   
    model = app.models.get('Outlets and Faceplates')
    
    url = raw_input("URL of Image: ")
    print model.predict_by_url(url)['outputs'][0]['data']['concepts']
       
    


def create_image_set(img_path, concepts):
    images = []
    for file_path in glob(os.path.join(img_path, '*.jpg')):
        img = ClImage(filename=file_path, concepts=concepts)
        images.append(img)
         
    return images

if __name__ == '__main__':
    main()