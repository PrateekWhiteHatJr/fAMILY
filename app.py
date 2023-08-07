from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def index1():
    relation = "Me"
    name = "Prateek"
    age = "16"
    img = "/me.png"
    return render_template("index.html",i=relation,j=name,k=age,l=img)

@app.route("/father")
def index2():
    relation = "Father"
    name = "Vikash"
    age = "40"
    img = "/father.png"
    return render_template("index.html",i=relation,j=name,k=age,l=img)

@app.route("/mother")
def index3():
    relation = "Mother"
    name = "Suman"
    age = "38"
    img = "/mother.png"
    return render_template("index.html",i=relation,j=name,k=age,l=img)

@app.route("/friend")
def index4():
    relation = "Friend"
    name = "Abhiraj"
    age = "17"
    img = "/friend.png"
    return render_template("index.html",i=relation,j=name,k=age,l=img)

if __name__ == "__main__":
    app.run()