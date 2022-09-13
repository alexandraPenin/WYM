from flask import Flask, render_template, request
from model_utils import resume_text

app = Flask(__name__)

@app.route("/")
def home():
	return render_template('index.html')


#app.run(debug=True, host='0.0.0.0')

@app.route("/about") 
def about():
    return render_template("about.html") 

@app.route("/model",methods=["GET","POST"]) 
def model():
    if request.method=="GET":
        return render_template("model.html")
    elif request.method=="POST":
        form_data_text=request.form['textmodel']
        form_data_resum=resume_text(form_data_text)
        print(form_data_resum)
    return render_template("model.html",resume=form_data_resum)

	
@app.route("/contact") 
def contact():
    return render_template("contact.html") 

@app.route("/contacted") 
def contacted():
    return render_template("contacted.html") 


if __name__ == "__main__":
    app.run(debug = True, host="0.0.0.0", port=5001) # démarrage de l’application
