from peewee import *

mysql_db= MySQLDatabase('arachnophobia', host='localhost', user='nina', passwd='pw' )

class MySQLModel (Model):
	class Meta:
        	database = mysql_db

# http://peewee.readthedocs.org/en/latest/peewee/api.html#CompositeKey



class User (MySQLModel):
	name = CharField(index=True)

class Topic (MySQLModel):
	name = CharField(index=True)

class Post (MySQLModel):
    text=CharField(index=True)
    timestamp=CharField()
    order=IntegerField()
    user= ForeignKeyField (User)	
    topic= ForeignKeyField (Topic)

class HTMLSite(MySQLModel):
      body=TextField (index=True)


def create_tables():	
    User.create_table()
    Topic.create_table()    
    Post.create_table()    
	
