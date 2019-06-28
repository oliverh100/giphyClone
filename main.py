from flask import Flask, render_template, request, url_for, flash
import random
from fuzzywuzzy import process
from db import *



app = Flask(__name__)
app.config['SECRET_KEY'] = '3d6f45a5fc12445dbac2f58c3b6c7cb1'
app.static_folder = 'static'



@app.route('/', methods = ['GET'])
def home():
	db_list = [tag.tag for tag in tags.select(tags.tag).distinct()]
	newTag = request.args.get('tagEntry')
	gifTag = request.args.get('gifTag')
	if newTag:
		num = random.randint(20, 10 ** 10)
		tags.create(id = num, tag = newTag)
		link.create(gif_id = int(gifTag[:-4]), tag_id = num)
	data = request.args.get('entry')
	if data:
		choice = search(data, db_list)
	else:
		choice = str(random.randint(1,10)) + ".gif"
	tagList = find_tag_list(choice, db_list)
	return render_template('home.html', gif = choice, tagList = tagList, filename = choice)



def search(data, db_list):
	data = data.lower()
	if data not in db_list:
		nearest = process.extract(data, db_list, limit = 1)[0][0]
		choice = random.choice(tags.get(tags.tag == nearest).gifs)
	else:
		choice = random.choice(tags.get(tags.tag == data).gifs)
	return choice.filename



def find_tag_list(choice, db_list):
	tagList = []
	for i in db_list:
		temp = [x.filename for x in tags.get(tags.tag == i).gifs]
		if choice in temp:
			tagList.append(i)
	return tagList





