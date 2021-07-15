from flask import Flask,render_template,request
import db
app = Flask(__name__)

@app.route('/',methods=["POST","GET"])
def create():
    if request.method=="POST":
         name = request.form.get('name')
         email = request.form.get('email')
         message = request.form.get('message')
         print(name,email,message)
         user = db.User()  
         user.name = name
         user.email = email
         user.message = message
         user.save()
    return render_template("index.html")

@app.route('/why',methods=["POST","GET"])
def why():
    return render_template("why.html")

if __name__ == "__main__":
    app.run(debug=True)
