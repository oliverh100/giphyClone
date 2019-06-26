from flask import Flask, render_template, request, url_for
import random
app = Flask(__name__)


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
	return render_template('search.html', title = 'search', data = '')


@app.route('/search/', methods = ['POST'])
def searchForm():
	data = request.form['entry']
	return render_template('search.html', title = 'search', data = data)