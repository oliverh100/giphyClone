from flask import Flask, render_template, request, url_for, flash
from random import randint
from fuzzywuzzy import process


app = Flask(__name__)
app.config['SECRET_KEY'] = '3d6f45a5fc12445dbac2f58c3b6c7cb1'
app.static_folder = 'static'



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

database_list = []
for i in database.values():
	for j in i:
		database_list.append(j)


@app.route('/', methods = ['GET'])
def home():
	data = request.args.get('entry')
	if data:
		flag = False
		options = []
		nearest = process.extract(data, database_list, limit = 1)[0][0]
		secondary_options = []
		for k, v in database.items():
			if data.lower() in v:
				flag = True
				options.append(k)
			if nearest.lower() in v:
				secondary_options.append(k)
		if not flag:
			num = randint(1, len(secondary_options))
			choice = secondary_options[num - 1]
			return render_template('home.html', flag = 'False', gif = "/static/library/" + choice + ".gif")
		else:
			num = randint(1, len(options))
			choice = options[num - 1]
			return render_template('home.html', flag = 'False', gif = "/static/library/" + choice + ".gif")
	else:
		rand = randint(1,10)
		return render_template('home.html', flag = 'False', gif = "/static/library/" + str(rand) + ".gif")





