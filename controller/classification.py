from flask import Blueprint, jsonify, request
from use_cases.predict import predict
user_bp = Blueprint('user', __name__)

@user_bp.route('/', methods=['GET'])
def listar_usuarios():
   print(predict("test/no_dr.png"))
   return jsonify(predict("test/no_dr.png"))
