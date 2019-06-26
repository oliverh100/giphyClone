from flask import Flask, render_template, request, url_for, flash
from random import randint


app = Flask(__name__)
app.config['SECRET_KEY'] = '3d6f45a5fc12445dbac2f59c3b6c7cb1'


gifs = {'dog': '1', 'pizza': '2', 'yawning': '3'}



@app.route('/', methods = ['GET'])
def home():
	data = request.args.get('entry')
	if data:
		if data.lower() not in gifs:
			return render_template('home.html', flag = 'True', gif = '')
		else:
			num = gifs[data]
			return render_template('home.html', flag = 'False', gif = "/static/library/" + num + ".gif")
	else:
		rand = randint(1,10)
		return render_template('home.html', flag = 'False', gif = "/static/library/" + str(rand) + ".gif")
