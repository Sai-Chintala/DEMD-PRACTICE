from flask import Flask, request
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)


@app.route('/')
def base_route():
    return "Welcome to Praxis"

@app.route('/my_name/<name>')
def print_name(name):
    return f"Happy learning {name} in Praxis Bangalore"

@app.route('/hello',methods = ["GET"])
def hello():
    
    """Lets try Swagger from  Flasgger
    ---
    parameters:
        - name: StudentName
          in: query
          type: string
          required: true 

        - name: RollNo
          in: query
          type: string
          required: true

    responses:
        200:
            description: The result is
    """

    try:
        stud_name = request.args.get("StudentName")
        numb = request.args.get("RollNo")
        
        return f"Student Name is {stud_name} and Roll Number is {numb}", 200

    except Exception as e:
        return f"Error occured with message : {e}", 401

if __name__ == "__main__":
    app.run(host = "0.0.0.0",port = 8000, debug = True)