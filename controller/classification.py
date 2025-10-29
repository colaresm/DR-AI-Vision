from flask import Blueprint, jsonify, request
from use_cases.predict import predict
from use_cases.segmentation import segment_hard_exudates
import cv2
import numpy as np

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
        cv2.imwrite("filename.png",segmented_image)
        return jsonify({"prediction":predict(img)})

    except Exception as e:
        return jsonify({"error": str(e)}), 500