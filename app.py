from flask import Flask,render_template,request,redirect
from pymongo import MongoClient

app = Flask(__name__)
my_client = MongoClient("localhost", 27017)
my_db= my_client["Clg_Administrations"]
students = my_db["students"]
callme = my_db["callme"]

@app.route("/", methods=["GET"])
def homepage():
    return render_template("index.html")

@app.route("/admissions", methods=["GET"])
def admissions():
    return render_template("admissions.html")

@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "POST":
        _id=request.form["id"]
        name=request.form["name"]
        email=request.form["email"]
        phone=request.form["phone"]
        percentage=request.form["percentage"]
        rank=request.form["rank"]
        course=request.form["course"]
        address=request.form["address"]

        students.insert_one({"id":_id, "name":name, "email":email, "phone":phone, "percentage":percentage, "rank":rank, "course":course, "address":address} )
        return redirect("/register")
    return render_template("register.html")

@app.route("/view", methods=["GET"])
def view():
    data = list(students.find())
    return render_template("view.html",output = data)

@app.route("/update", methods=["GET","POST"])
def update():
    if request.method == "POST":
        _id = request.form["id"]
        field = request.form["field"]
        new_data = request.form["new_data"]
        students.update_one({"id":_id},{"$set":{field:new_data}})
        return redirect("/update")
    return render_template("update.html")


@app.route("/delete", methods=["GET","POST"])
def delete():
    if request.method == "POST":
        _id = request.form["id"]
        students.delete_one({"id":_id})
    return render_template("delete.html")

@app.route("/campus", methods=["GET","POST"])
def campus():
    return render_template("campus.html")

@app.route("/callme",methods = ["GET","POST"])
def call_me():
    if request.method ==  "POST":
        name = request.form["name"]
        email = request.form["email"]
        num = request.form["num"]
        course = request.form["course"]

        callme.insert_one({"name":name, "email" :email, "num": num, "course": course})
        return redirect("/")
    return render_template("index.html")
@app.route("/callmedata", methods =["GET"])
def CallMe():
    data = list(callme.find())
    return render_template("CallMe.html",output = data)

app.run(port=5001, debug=True)