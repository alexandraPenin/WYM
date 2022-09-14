
from flask import Flask, render_template, request
from model_utils import resume_text
import psycopg2
import database
import db_utils
from db_utils import User, pgdb

app = Flask(__name__)
mydb = pgdb("localhost",5432)

@app.route("/")
def home():
	return render_template('index.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    print('ping')
    if request.method == 'GET':
        return render_template('contact.html')
    elif request.method == 'POST':
        nom = request.form['nom']
        prenom = request.form['prenom']
        telephone = request.form['telephone']
        mail = request.form['mail']
        print(nom, prenom, mail, telephone)
        user = User(nom, prenom, mail, telephone)
        
        mydb.connect()
        mydb.insert_user(user)    
        mydb.disconnect()
        return render_template('contact.html')

@app.route('/contacted')
def contacted():
    mydb.connect()
    users = mydb.get_users()
    print('user')
    print(users[0][0])
    mydb.disconnect()
    return render_template('contacted.html', users=users[0])


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


if __name__ == "__main__":
    app.run(debug = True, host="0.0.0.0", port=5001) # démarrage de l’application