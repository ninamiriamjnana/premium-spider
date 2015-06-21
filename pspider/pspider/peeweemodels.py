from peewee import *

mysql_db= MySQLDatabase('arachnophobia', host='localhost', user='user')

class MySQLModel (Model):
	class Meta:
        	database = mysql_db

# http://peewee.readthedocs.org/en/latest/peewee/api.html#CompositeKey



class User (MySQLModel):
	name = CharField(index=True)

class Topic (MySQLModel):
	name = CharField(index=True)

class HTMLPage(MySQLModel):
      url=CharField(index=True)
      body=TextField ()

class Date_Tab(MySQLModel):
    year=IntegerField()
    month=IntegerField()
    day=IntegerField()

    class Meta:
		    index=(
				    (('year', 'month', 'day'), True),)
    

class Post (MySQLModel):
	pid=IntegerField(index=True)
	text=CharField()
	timestamp=CharField()
	date=CharField()
	order=IntegerField()
	user= ForeignKeyField (User)	
	topic= ForeignKeyField (Topic)
	htmlpage=ForeignKeyField (HTMLPage)
	date_tab=ForeignKeyField(Date_Tab)

class TopicUserNode (MySQLModel):
	original_id=IntegerField()
	name=CharField()
	typ=IntegerField()







def create_tables():	
    User.create_table()
    Topic.create_table()    
    Date_Tab.create_table()
    HTMLPage.create_table()
    Post.create_table()   
    TopicUserNode.create_table()
    
	
