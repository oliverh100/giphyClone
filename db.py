from peewee import *



db = SqliteDatabase('static/gifs.db')



class gif(Model):
	filename = CharField()

	class Meta:
		database = db
		db_table = 'gif2'


defered_link = DeferredThroughModel()


class tags(Model):
	tag = CharField()
	gifs = ManyToManyField(gif, backref='tags', through_model=defered_link)

	class Meta:
		database = db
		db_table = 'tags2'



class link(Model):
	gif = ForeignKeyField(gif, backref = 'tag_links')
	tag = ForeignKeyField(tags, backref = 'gif_links')

	class Meta:
		database = db
		db_table = 'link'


defered_link.set_model(link)

