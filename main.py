from flask import Flask, render_template, request, url_for, flash
from random import randint
from fuzzywuzzy import fuzz


app = Flask(__name__)
app.config['SECRET_KEY'] = '3d6f45a5fc12445dbac2f58c3b6c7cb1'
app.static_folder = 'static'


gifs = {'dog': '1', 'pizza': '2', 'yawning': '3'}

database = {
	'1': ['dog', 'book'],
	'2': ['pizza'],
	'3': ['yawn', 'hat'],
	'4': ['run', 'charlie kelly'],
	'5': ['zoom', 'nod'],
	'6': ['laugh'],
	'7': ['worried'],
	'8': ['laugh'],
	'9': ['laugh'],
	'10': ['laugh', 'ricky gervais'],
}

'''
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
'''

@app.route('/', methods = ['GET'])
def home():
	data = request.args.get('entry')
	if data:
		flag = False
		options = []
		for k, v in database.items():
			if data.lower() in v:
				flag = True
				options.append(k)
		if not flag:
			return render_template('home.html', flag = 'True', gif = '')
		else:
			num = randint(1, len(options))
			choice = options[num - 1]
			return render_template('home.html', flag = 'False', gif = "/static/library/" + choice + ".gif")
	else:
		rand = randint(1,10)
		return render_template('home.html', flag = 'False', gif = "/static/library/" + str(rand) + ".gif")





