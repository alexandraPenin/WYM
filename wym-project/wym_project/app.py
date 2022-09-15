import os

from flask import Flask, render_template, request
import psycopg2

from wym_project.model_utils import resume_text
from wym_project.db_utils import User, pgdb
import time


if os.getenv("DOCKER_BUILD"):
    db_host = os.getenv("DB_HOST")
    model_host = os.getenv("MODEL_HOST")
else:
    db_host = "localhost"
    model_host = "localhost"

print(f"{db_host=}")
print(f"{model_host=}")

mydb = pgdb(db_host, 5432)

# creation de la table 'users' (si elle n'existe pas déjà)
mydb.connect()
mydb.create_users_table()    
mydb.disconnect()


app = Flask(__name__)


@app.route("/")
def home():
	return render_template('index.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
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
    mydb.disconnect()
    return render_template('contacted.html', users=users)


@app.route("/about") 
def about():
    return render_template("about.html") 


@app.route("/model",methods=["GET","POST"]) 
def model():
    if request.method=="GET":
        return render_template("model.html")
    elif request.method=="POST":
        form_data_text=request.form['textmodel']
        taille_text=len(form_data_text)
        second_start=time.time()
        print("The biginning of the chrono:", second_start)
        form_data_resum=resume_text(form_data_text, host=model_host)
        second_end=time.time()
        result_time=second_end-second_start
        print("The end of the chrono:", second_end)
        print("The time of execution of your request is:",result_time)
        print(form_data_resum)

    return render_template("model.html", resume=form_data_resum['summary_text'][0],result=result_time,taille_text=taille_text)


def main():
  app.run(debug = True, host="0.0.0.0", port=5001) # démarrage de l’application


if __name__ == "__main__":
  main()
