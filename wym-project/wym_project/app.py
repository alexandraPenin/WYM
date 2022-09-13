from flask import Flask, render_template, request
import psycopg2
import database
import db_utils
from db_utils import User, pgdb

app = Flask(__name__)
mydb = pgdb("localhost",5432)

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'GET':
        return render_template('form.html')
    elif request.method == 'POST':
        nom = request.form['nom']
        prenom = request.form['prenom']
        telephone = request.form['telephone']
        mail = request.form['mail']

        user = User(nom, prenom, mail, telephone)
        mydb.connect()
        mydb.insert_user(user)    
        mydb.disconnect()
        return render_template('form.html')


app.run(debug=True, host='0.0.0.0')
