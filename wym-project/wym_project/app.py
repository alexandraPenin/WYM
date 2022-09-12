from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/")
def home():
	return render_template('index.html')


#app.run(debug=True, host='0.0.0.0')

@app.route("/about") 
def about():
    return render_template("about.html") 

@app.route("/model") 
def model():
    return render_template("model.html") 
	
@app.route("/contact") 
def contact():
    return render_template("contact.html") 

@app.route("/contacted") 
def contacted():
    return render_template("contacted.html") 


if __name__ == "__main__":
    app.run(debug = True, host="0.0.0.0") # démarrage de l’application
