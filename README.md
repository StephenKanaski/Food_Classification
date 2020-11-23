Food Classification
Emily Zhu, Raymond Garskovas, Stephen Kanaski, Surabhi Mukati

![alt text](https://github.com/spunase/Food_Classification/blob/main/static/images/default.jpg)

# Food_Classification - Overview of project

Addressable Market:
- Food posts are among the most popular images on social media platforms. Hashtags such as #foodie, #food, #foodporn, #foodphotography relate to hundreds of thousands of images per day

Project Scope:
- An application which can take an image of food and output what the category of food is

Anticipated Benefits:
- Identification of food which users see online for their own reference
- Identification of food which a user can then research to avoid potential allergies

# File directory

## Key Files

Data cleaning and pre-processing:

- Pickle.pynb – Initial image processing file which cycles through the images folder and generates pkl files

- Sequential.pynb – Processing file which takes pkl files generated from Pickle.pynb 

- Category.json – JSON file which contains the 101 categories of food


Application:

- App.py – Application file which runs the flask routes to handle the input and output


Models:

- MobileNet.h5 – MobileNet model output file

- Resnet50.h5 – ResNet50 model output file

## Reference Folders
- Images: Images folder contains a sample set of images which the model trained

- Templates: Front end HTML files

# Model detail
CNN Sequential Model - For this model we are converting image data in to binary in pickle notebook and storing it in X.pickle(image data) and y.pickle(labels). In this model we tried 7 layers and got 46% testing accuracy.
