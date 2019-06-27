from db import *
db.connect()
first = gif.get(gif.tag == 'dog')
print(first.filename)
db.close()