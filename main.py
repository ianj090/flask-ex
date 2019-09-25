from flask import Flask, render_template
import yaml

app = Flask(__name__)

# @app.route("/") # home page
# def home():
#     return "Hello!"

edad = 19

with open("info.yml", 'r') as f:
    line = f.readline()
    while line:
        print("{}".format(line.strip()))
        line = f.readline()



@app.route("/") # info page
def info():
    return render_template("info.html")

@app.route("/academics") # info page
def academics():
    return render_template("academics.html")

@app.route("/work") # info page
def work():
    return render_template("work.html")

@app.route("/contact") # info page
def contact():
    return render_template("contact.html")
    
if __name__ == "__main__":
    app.run(debug=True)
