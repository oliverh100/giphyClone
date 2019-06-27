from flask import Flask, render_template, request, url_for, flash
import random
from fuzzywuzzy import process
from db import *



app = Flask(__name__)
app.config['SECRET_KEY'] = '3d6f45a5fc12445dbac2f58c3b6c7cb1'
app.static_folder = 'static'


'''
temp = gif.select()
db_list = [''] * len(temp)
for i in range(len(temp)):
	db_list[i] = temp[i].tag
'''

'''
@app.route('/', methods = ['GET'])
def home():
	data = request.args.get('entry')
	if data:
		data = data.lower()
		if data not in db_list:
			nearest = process.extract(data, db_list, limit = 1)[0][0]
			secondary_options = gif.select().where(gif.tag == nearest)
			choice = random.choice(secondary_options).filename
		else:
			options = gif.select().where(gif.tag == data)
			choice = random.choice(options).filename
	else:
		choice = str(random.randint(1,10)) + ".gif"
	return render_template('home.html', gif = "/static/library/" + choice)

'''

@app.route('/', methods = ['GET'])
def home():
	data = request.args.get('entry')
	if data:


		tagIDs = tags.select().where(tags.tag == data)

		TAGID = random.choice(tagIDs).id
		print(TAGID)
		GIFIDs = link.get(link.tag == TAGID)
		GIFID = GIFIDs.id
		print(GIFID)
		filename = gif.get(gif.id == GIFID)
		print(filename.filename)
		choice = filename.filename



	return render_template('home.html', gif = "/static/library/" + choice)





