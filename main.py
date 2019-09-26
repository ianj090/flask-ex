from flask import Flask, render_template
import yaml

app = Flask(__name__)

with open("info.yml", 'r') as f:
    file = f.read()

my_dict = yaml.safe_load(open("info.yml"))

@app.route("/") # info page
def info():
    return render_template(
    "info.html", 
    nombre = my_dict["nombre"],
    edad = my_dict["edad"],
    estado_civil = my_dict["estado_civil"],
    correo = my_dict["correo"],
    direccion = my_dict["direccion"],
    nacionalidad = my_dict["nacionalidad"],
    sobre_mi = my_dict["sobre_mi"],
    imagen = my_dict["imagen"]
    )

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
