from peewee import *

db = SqliteDatabase('static/gifs.db')



class gif(Model):
	# id = IntegerField()
	filename = CharField()

	class Meta:
		database = db
		db_table = 'gif2'


class tags(Model):
	# id = IntegerField()
	tag = CharField()

	class Meta:
		database = db
		db_table = 'tags2'


class link(Model):
	# gif_id = ForeignKeyField(gif, backref = 'link')
	# tag_id = ForeignKeyField(tags, backref = 'link')

	# id = IntegerField()
	tag = IntegerField()

	class Meta:
		database = db
		db_table = 'link2'