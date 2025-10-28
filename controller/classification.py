from flask import Blueprint, jsonify, request
from use_cases.predict import predict
import time
import cv2
import numpy as np
import base64

api_bp = Blueprint('api', __name__)

@api_bp.route('/s', methods=['GET'])
def healthy():
   print("sjnjnjknkn")
   return jsonify("true")

@api_bp.route('/predict-and-segment', methods=['POST'])
def predict_and_segment():
    try:
        if 'imagem' not in request.files:
            return jsonify({"error": "Field 'imagem' is required"}), 400

        file = request.files['imagem']
        file_bytes = np.frombuffer(file.read(), np.uint8)
        img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

        if img is None:
            return jsonify({"error": "Failed to decode image"}), 400
   
        return jsonify({"prediction":predict(img)})

    except Exception as e:
        return jsonify({"error": str(e)}), 500