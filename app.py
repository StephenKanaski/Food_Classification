
from flask import Flask, request, jsonify, render_template
from tensorflow.keras.models import load_model
from keras.preprocessing import image
import PIL
import numpy as np
import os
import json

IMAGES_FOLDER = os.path.join('static', 'images')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = IMAGES_FOLDER
# load the MobileNet model as it has the highest accuracy amongst all the models tested
model = load_model('MobileNet.h5')


@app.route('/')
@app.route('/index')
def home():
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'default.jpg')
    return render_template("index.html", prediction_img = full_filename)

@app.route('/predict',methods=['GET', 'POST'])  
def predict():

    # For rendering results on HTML GUI after predicting using the model
    
    # build the path to where the user images will be stored for later retrieval
    PATH = os.getcwd()
    # img_folder_path = os.path.join(PATH, "images")

    # get the image file input by the user 
    f = request.files['file']
    
    # build the image path and save it in the designated folder
    img_url = os.path.join(app.config['UPLOAD_FOLDER'], f.filename)
    f.save(img_url)
    
    # preprocess the image as an array after adjusting it to target model's size requirement
    image_predict = image.load_img(img_url, target_size=(224,224))
    image_predict = image.img_to_array(image_predict)
    image_predict = np.expand_dims(image_predict, axis=0)

    # get the probability prediction and category index corresponding to it
    y_prob = model.predict(image_predict) 
    y_classes = int(y_prob.argmax(axis=-1))


    # read the category.json file to convert the category index into a label
    with open('category.json') as json_file:
          CATEGORY = json.load(json_file)
    output = CATEGORY[y_classes]

    return render_template('index.html', prediction_text=output, prediction_img=img_url)



if __name__ == "__main__":
    app.run(debug=True)
