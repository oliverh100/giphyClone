from flask import Flask, render_template
import random
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html', title = 'index')

@app.route('/home/')
def home():
	rand = random.randint(1,10)
	return render_template('home.html', title = 'home', num = rand, gif = "/static/library/" + str(rand) + ".gif")