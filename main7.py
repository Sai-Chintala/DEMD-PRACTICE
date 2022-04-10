from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def base_route():
    return "Welcome to Praxis"

@app.route('/my_name/<name>')
def print_name(name):
    return f"Happy learning {name} in Praxis Bangalore"

@app.route('/hello',methods = ["GET", "POST"])
def hello():
    stud_name = request.args.get("StudentName")
    numb = request.args.get("RollNo")
    
    return f"Student Name is {stud_name} and Roll Number is {numb}"

if __name__ == "__main__":
    app.run(host = "0.0.0.0",port = 8000, debug = True)