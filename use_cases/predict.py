import cv2
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from infrastructure.label_mapper import get_label

model = load_model("models/clf.keras")

def predict(img):
    img = preprocess(img)
    prediction = model.predict(img)
    class_number = int(np.argmax(prediction))
    label = get_label(class_number)
    return label

def preprocess(img):
    #img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (224, 224))
    img = preprocess_input(img)
    img = np.expand_dims(img, axis=0)
    return img
