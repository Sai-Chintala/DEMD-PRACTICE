from flask import Flask, request
from flasgger import Swagger
import pickle
from sklearn.linear_model import LogisticRegression

app = Flask(__name__)
Swagger(app)

pickled_model_file = open("pickle_iris_model.pkl","rb")
classifier = pickle.load(pickled_model_file)

@app.route('/')
def home_page():
    return "Welcome to Iris Classifier"

@app.route('/predict')
def predict_flower():

    """Predict the Iris flower category
     ---
    parameters:
        - name : Sepal_width
          in : query
          type : number 
          required : true

        - name : Sepal_length
          in : query
          type : number 
          required : true

        - name : Petal_width
          in : query
          type : number 
          required : true

        - name : Petal_length
          in : query
          type : number 
          required : true
    
    responses:
       200:
            description: The result is

    """

    sw = request.args.get("Sepal_width")
    sl = request.args.get("Sepal_length")
    pw = request.args.get("Petal_width")
    pl = request.args.get("Petal_length") 

    result = classifier.predict([[sw,sl,pw,pl]])

    return f"The prediction is that flower belongs to class{result}"


if __name__ == "__main__":
    app.run(host = "0.0.0.0",port = 8000, debug = True)




