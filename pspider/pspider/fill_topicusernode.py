
from peewee import *
from peeweemodels import *

def writetotable():
	for topic in Topic.select():
		TopicUserNode.create(original_id=topic.id, name=topic.name, typ=0)

	for user in User.select():
		TopicUserNode.create(original_id=user.id, name=user.name, typ=1)
