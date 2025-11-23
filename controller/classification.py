from flask import Blueprint, jsonify, request
from use_cases.predict import predict
from use_cases.segmentation import segment_hard_exudates
import cv2
import numpy as np
import base64


api_bp = Blueprint('api', __name__)

@api_bp.route('/healthys', methods=['GET'])
def healthy():
   return jsonify({"prediction":True})

@api_bp.route('/predict-and-segment-single', methods=['POST'])
def predict_and_segment_single():
    try:
        if 'imagem' not in request.files:
            return jsonify({"error": "Field 'imagem' is required"}), 400

        file = request.files['imagem']
        file_bytes = np.frombuffer(file.read(), np.uint8)
        img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

        if img is None:
            return jsonify({"error": "Failed to decode image"}), 400
        
        segmented_image = segment_hard_exudates(img)

        overlay = create_overlay(img, segmented_image)
        cv2.imwrite("tes.png",overlay)
        overlay_base64 = encode_image_to_base64(overlay)      
       
        return jsonify({"prediction":predict(img), "overlay_image": overlay_base64})

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

def create_overlay(original, mask):
    original = cv2.resize(original,(256,256))
    mask_255 = (mask * 255).astype(np.uint8)

 
    mask_color = cv2.cvtColor(mask_255, cv2.COLOR_GRAY2BGR)
  
    color = np.array([0, 255, 0], dtype=np.uint8)

    mask_applied = np.where(mask_color == 255, color, 0)

    overlay = cv2.addWeighted(original, 0.7, mask_applied, 0.3, 0)

    return overlay



def encode_image_to_base64(image):
    _, buffer = cv2.imencode(".png", image)
    return base64.b64encode(buffer).decode("utf-8")
