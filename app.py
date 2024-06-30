from flask import Flask, render_template, request, jsonify
from PIL import Image
import base64
from io import BytesIO
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array

jsonData = []

def open_image_from_base64(base64_string):

    img_data = base64_string.split(',')[1]
    img_bytes = base64.b64decode(img_data)
    img = Image.open(BytesIO(img_bytes))

    return img

app = Flask(__name__)

model = load_model('model.h5')
emotion_labels = ['angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral']

def prepare_image(image, target_size):
    if image.mode != "RGB":
        image = image.convert("RGB")
    image = image.resize(target_size)
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    image = image / 255.0
    return image

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/vision', methods=['POST'])
def index():
    return render_template('vision.html', error = '')

@app.route('/getData', methods=['POST'])
def parse_request():
    data = request.get_json()
    if data:
        jsonData.append(data)
        image = jsonData[0]  
        return jsonify({'image': image}), 200  
    else:
        return jsonify({'error': 'No JSON data received'}), 400

@app.route('/sendData', methods=['POST'])
def send_data():
    if not jsonData:
        return render_template('vision.html', error = "Please click a picture")
    base64_image_string = jsonData[0]
    image = open_image_from_base64(str(base64_image_string))
    processed_image = prepare_image(image, target_size=(48, 48))
    print('Image processed')
    prediction = model.predict(processed_image)
    predicted_class = emotion_labels[np.argmax(prediction[0])]
    print(predicted_class)
    return render_template('show_result.html', prediction = predicted_class)

if __name__ == '__main__':
    app.run(port=1989)