from flask import Flask, render_template, request, url_for, flash
import random
app = Flask(__name__)
app.config['SECRET_KEY'] = '3d6f45a5fc12445dbac2f59c3b6c7cb1'

gifs = {'dog': '1', 'pizza': '2', 'yawning': '3'}


@app.route('/')
def home():
	rand = random.randint(1,10)
	return render_template('home.html', title = 'home', num = rand, gif = "/static/library/" + str(rand) + ".gif", data  = '')


@app.route('/random/')
def randomGIF():
	rand = random.randint(1,10)
	return render_template('random.html', title = 'random', num = rand, gif  = "/static/library/" + str(rand) + ".gif")


@app.route('/search/')
def search():
	return render_template('search.html', title = 'search', data = '', gif = '')


@app.route('/search/', methods = ['POST'])
def searchForm():
	data = request.form['entry']
	if data.lower() not in gifs:
		return render_template('search.html', title = 'search', data = data, flag = 'True', gif = '')
		print('ERROR')
	else:
		num = gifs[data]
		return render_template('search.html', title = 'search', data = data, flag = 'False', gif = "/static/library/" + num + ".gif")
	return render_template('search.html', title = 'search', data = data, flag = 'False', gif = '')