#from use_cases.predict import predict

#print(predict("test/no_dr.png"))
from flask import Flask
from controller.classification import user_bp 

app = Flask(__name__)


app.register_blueprint(user_bp , url_prefix='/user')

if __name__ == '__main__':
    app.run(debug=True)
