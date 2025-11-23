from flask import Flask
from controller.classification import api_bp 
from flask_cors import CORS

app = Flask(__name__)

CORS(app)
app.register_blueprint(api_bp , url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)
