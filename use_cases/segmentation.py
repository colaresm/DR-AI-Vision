import cv2
from tensorflow.keras.models import load_model
import numpy as np

def segment_hard_exudates(image):
    model = load_model("models/hard_exudates_segmentation.keras")
    image = cv2.resize(image, (256, 256))
    image = np.array(image)/255.0
    segmented_image = model.predict(np.expand_dims(image, axis=0))
    return segmented_image