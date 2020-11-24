# Food Classification Application
Emily Zhu, Raymond Garskovas, Stephen Kanaski, Surabhi Mukati

![alt text](https://github.com/spunase/Food_Classification/blob/main/static/images/default.jpg)

## Overview of project

Addressable Market:
- Food posts are among the most popular images on social media platforms. Hashtags such as #foodie, #food, #foodporn, #foodphotography relate to hundreds of thousands of images per day

Project Scope:
- An application which can take an image of food and output what the category of food is

Anticipated Benefits:
- Identification of food which users see online for their own reference
- Identification of food which a user can then research to avoid potential allergies

Data Source:
https://www.kaggle.com/kmader/food41

## File directory

### Key Files

Data cleaning and pre-processing:

- Pickle.ipynb – Initial image processing file which cycles through the images folder and generates pkl files

- Sequential.ipynb – Processing file which takes pkl files generated from Pickle.ipynb 

- MobileNet.ipynb –  Notebook to preprocess, train, and test the model

- Category.json – JSON file which contains the 101 categories of food


Application:

- App.py – Application file which runs the flask routes to handle the input and output


Models:

- MobileNet.h5 – MobileNet model output file

- Resnet50.h5 – ResNet50 model output file

- food_seq_model.h5 - CNN Sequential model output file

### Reference Folders
- Images - Images folder contains a sample set of images which the model trained

- Templates - Front end HTML files
