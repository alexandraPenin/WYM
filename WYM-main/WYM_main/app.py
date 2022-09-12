from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/")
def home():

	return render_template('index.html')
	
@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
	if request.method == 'GET':
		return render_template('form.html')
	elif request.method == 'POST':
		form_data_f = request.form['fname']
		form_data_l = request.form['lname']

		with open("dataset.txt", "a") as f:
			f.write(form_data_f)
			f.write(';')
			f.write(form_data_l)
			f.write('\n')


		return render_template('form.html', titre = 'abcd')
	return render_template('form.html')

@app.route('/gateaux')
def gateaux():
	return render_template('gateaux.html')

app.run(debug=True, host='0.0.0.0')
