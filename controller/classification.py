from flask import Blueprint, jsonify, request
from use_cases.predict import predict
user_bp = Blueprint('user', __name__)
import time
@user_bp.route('/', methods=['GET'])
def listar_usuarios():
   start = time.time()
   print(predict("test/no_dr.png"))
   end = time.time()
   print("time",end-start)
   return jsonify(predict("test/no_dr.png"))
