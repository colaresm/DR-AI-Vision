import cv2
from tensorflow.keras.models import load_model
import numpy as np
import keras.backend as K

from keras.saving import register_keras_serializable
import tensorflow as tf

@tf.keras.utils.register_keras_serializable()
def jaccard_index(y_true, y_pred):
    """Calculates the Jaccard index (IoU), useful for evaluating the model's performance."""
    y_true_f = tf.reshape(tf.cast(y_true, tf.float32), [-1])  # Flatten and cast ground truth
    y_pred_f = tf.reshape(tf.cast(y_pred, tf.float32), [-1])  # Flatten and cast predictions
    intersection = tf.reduce_sum(y_true_f * y_pred_f)  # Compute intersection
    total = tf.reduce_sum(y_true_f) + tf.reduce_sum(y_pred_f) - intersection  # Total pixels
    return (intersection) / (total)

@tf.keras.utils.register_keras_serializable()
def dice_coefficient(y_true, y_pred):
    # Flatten and cast true and predicted masks to float32
    y_true_f = tf.reshape(tf.cast(y_true, tf.float32), [-1])  # Flatten and cast y_true to float32
    y_pred_f = tf.reshape(tf.cast(y_pred, tf.float32), [-1])  # Flatten and cast y_pred to float32

    # Calculate the intersection between the true and predicted masks
    intersection = tf.reduce_sum(y_true_f * y_pred_f)

    # Calculate the Dice coefficient using the formula
    return (2. * intersection) / (tf.reduce_sum(y_true_f) + tf.reduce_sum(y_pred_f))

@tf.keras.utils.register_keras_serializable()
def dice_loss(y_true, y_pred):
    smooth = 1e-6
    intersection = tf.reduce_sum(y_true * y_pred)
    return 1 - (2. * intersection + smooth) / (tf.reduce_sum(y_true) + tf.reduce_sum(y_pred) + smooth)

@tf.keras.utils.register_keras_serializable()
def focal_loss(alpha=0.25, gamma=2.0):
    def focal(y_true, y_pred):
        y_pred = tf.clip_by_value(y_pred, 1e-6, 1.0 - 1e-6)  # Evita log(0)
        bce = -y_true * tf.math.log(y_pred) - (1 - y_true) * tf.math.log(1 - y_pred)
        weight = alpha * y_true * tf.math.pow(1 - y_pred, gamma) + (1 - alpha) * (1 - y_true) * tf.math.pow(y_pred, gamma)
        return tf.reduce_mean(weight * bce)
    return focal



@tf.keras.utils.register_keras_serializable()
def combined_loss(alpha=0.25, gamma=2.0, dice_weight=0.5, focal_weight=0.5):
    def loss(y_true, y_pred):
        return dice_weight * dice_loss(y_true, y_pred) + focal_weight * focal_loss(alpha, gamma)(y_true, y_pred)
    return loss

import cv2
import numpy as np
from tensorflow.keras.models import load_model

def segment_hard_exudatess(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    model = load_model("models/hard_exudates_segmentation.keras", custom_objects={'loss': combined_loss})
    if len(image.shape) == 2:
        image = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)
    elif image.shape[2] == 1:
        image = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)
    image = cv2.resize(image, (256, 256))
    image = image.astype(np.float32) / 255.0
    input_image = np.expand_dims(image, axis=0)
    segmented_image = model.predict(input_image)[0]
    if segmented_image.shape[-1] == 2:
        segmented_image = segmented_image[..., 1]
    segmented_image = (segmented_image > 0.5).astype(np.uint8)
    return segmented_image

img = cv2.imread("./test/olho-esquerdo-8.jpg")

import matplotlib.pyplot as plt
segmented = segment_hard_exudatess(img)

plt.imshow(segmented)
plt.show()


