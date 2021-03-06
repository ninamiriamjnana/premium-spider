from peeweemodels import *

import matplotlib.pyplot as plt

from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})

import numpy as np

import ipdb

import csv

import itertools

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

"""
select count(distinct topic.id), date_tab.year from topic inner join post on post.topic_id=topic.id inner join date_tab on date_tab.id=post.date_tab_id group by date_tab.year; 
"""
"""
def yeartopic():
    yquery=(Date_Tab.select(fn.Distinct(Date_Tab.year)).order_by(Date_Tab.year))
    year=[]
    for x in yquery:
        year.append(x.year)
    
    for y in year:
         tquery=(Topic.select(Date_Tab.year,fn.Count(fn.Distinct(Topic.id)).join(Post).join(Date_Tab).where(Date_Tab.year=='2015').group_by(Date_Tab.year))
   

myquery=(Date_Tab.select(Date_Tab.id, fn.Count(fn.Distinct(Topic.id)).alias('count')).join(Post).join(Topic).where(Date_Tab.year=='2015').group_by(Date_Tab.id))


select distinct count(topic.id), date_tab.id from topic inner join post on topic.id=post.topic_id inner join date_tab on date_tab.id=post.date_tab_id where date_tab.year='2015'group by date_tab.id;


    
    count_topic=[] 
    x=myquery[0]
    bleib_year=x.year
    year.append(x.year)
    zwischen_count=0  
    frisch_aus_else=0 
     
    for x in myquery:
        if x.year==bleib_year:
            if frisch_aus_else==1:
                zwischen_count+=aktueller_count
            zwischen_count+=x.count
            frisch_aus_else=0
        
        elif x.year!=bleib_year and frisch_aus_else==1:
            #ipdb.set_trace() 
            count_topic.append(aktueller_count)
            year.append(x.year)
            zwischen_count+=x.count
            frisch_aus_else=0
      
        elif x.year!=bleib_year and frisch_aus_else==0:
            #ipdb.set_trace() 
            count_topic.append(zwischen_count) 
            year.append(x.year)
            bleib_year=x.year
            zwischen_count=0 
            aktueller_count=x.count 
            frisch_aus_else=1
    #ipdb.set_trace() 
    
    count_topic.append(zwischen_count)

    print year
    print count_topic



def year_count_topic():
    myquery=(Date_Tab.select(Date_Tab.id, Date_Tab.year, fn.Count(fn.Distinct(Topic.id)).alias('count')).join(Post).join(Topic).group_by(Date_Tab.year).order_by(Date_Tab.year))
    


    year=[]
    count_topic=[] 
    x=myquery[0]
    bleib_year=x.year
    year.append(x.year)
    zwischen_count=0  
    frisch_aus_else=0 
     
    for x in myquery:
        if x.year==bleib_year:
            if frisch_aus_else==1:
                zwischen_count+=aktueller_count
            zwischen_count+=x.count
            frisch_aus_else=0
        
        elif x.year!=bleib_year and frisch_aus_else==1:
            #ipdb.set_trace() 
            count_topic.append(aktueller_count)
            year.append(x.year)
            zwischen_count+=x.count
            frisch_aus_else=0
      
        elif x.year!=bleib_year and frisch_aus_else==0:
            #ipdb.set_trace() 
            count_topic.append(zwischen_count) 
            year.append(x.year)
            bleib_year=x.year
            zwischen_count=0 
            aktueller_count=x.count 
            frisch_aus_else=1
    #ipdb.set_trace() 
    
    count_topic.append(zwischen_count)
    i=0
    for x in count_topic:
        i+=x
    print i
        
      

    fig= plt.figure(facecolor="white")
    ax = fig.add_subplot(111, axisbg="white")
    ax.spines["top"].set_visible(False)  
    ax.spines["right"].set_visible(False) 
    ax.get_xaxis().tick_bottom()  
    ax.get_yaxis().tick_left() 
    ax.set_title('Number of Topics per Year')
    ax.set_xlabel('Year')
    ax.set_ylabel('Number of Topics')
    
    index = np.arange(len(year))
    bar_width = 0.35
    
    t=plt.bar(index, count_topic, color="#3F5D7D")
    
    plt.xticks(index + bar_width,year, rotation=90)
    
    plt.show()

"""    

def user_count_topic():
	myquery=(User.select(User.id, User.name, fn.Count(fn.Distinct(Topic.id)).alias('count')).join(Post).join(Topic).group_by(User.id).order_by(fn.Count(fn.Distinct(Topic.id)).desc()))	

	namen=[]
	namen_id=[]
	count_x=[]
	count_q=0
    
	for x in myquery:
		count_x.append(x.count)
		print x.id
        
		print x.count
		namen_id.append(x.id)
		namen.append(x.name)
		count_q+=1
	keys = namen
	values = count_x
	adict = dict(itertools.izip(keys,values))

	for x in adict:
		print x

	with open('user_count_topic.csv', 'wb') as f:
		writer = csv.writer(f)
		for key, value in adict.items():
			writer.writerow([key, value])
   
   
	fig= plt.figure(facecolor="white")
	ax = fig.add_subplot(111, axisbg="white")
	ax.spines["top"].set_visible(False)  
	ax.spines["right"].set_visible(False) 
	ax.get_xaxis().tick_bottom()  
	ax.get_yaxis().tick_left() 
	ax.set_title('Number of Topics per User')
	ax.set_xlabel('User')
	ax.set_ylabel('Number of Topics')
	index = np.arange(count_q)
	bar_width = 0.35
    
	t=plt.bar(index, count_x, color="#3F5D7D")
    
	plt.xticks(index + bar_width,namen, rotation=90)
    
	plt.show()

def topic_count_user():

    
    myquery=(Topic.select(Topic.id, Topic.name, fn.Count(fn.Distinct(User.id)).alias('count')).join(Post).join(User).group_by(Topic.id).order_by(fn.Count(fn.Distinct(User.id)).desc(), Topic.id).limit(30))

    #query = Topic.select().annotate(Post).order_by(Post)
    namen=[]
    namen_id=[]
    count_x=[]
    
    for x in myquery:
        count_x.append(x.count)
        print x.id
        
        print x.count
        namen_id.append(x.id)
        namen.append(x.name)

    # muss namen und count_x in ein dict schreiben?

    keys = namen
    values = count_x
    adict = dict(itertools.izip(keys,values))

    for x in adict:
        print x

    with open('topic_count_user.csv', 'wb') as f:
        writer = csv.writer(f)
        for key, value in adict.items():
            writer.writerow([key, value])
   
    fig= plt.figure(facecolor="white")
    ax = fig.add_subplot(111, axisbg="white")
    ax.spines["top"].set_visible(False)  
    ax.spines["right"].set_visible(False) 
    ax.get_xaxis().tick_bottom()  
    ax.get_yaxis().tick_left() 
    ax.set_title('Number of Users per Topic')
    ax.set_xlabel('Topic')
    ax.set_ylabel('Number of Users')
    index = np.arange(30)
    bar_width = 0.35
    
    t=plt.bar(index, count_x, color="#3F5D7D")
    
    plt.xticks(index + bar_width,namen, rotation=90)
    
    plt.show()




def topic_count_posts():


    
    myquery=(Topic.select(Topic.id, Topic.name, fn.Count(Post.id).alias('count')).join(Post).group_by(Topic.id).order_by(fn.Count(Post.id).desc(), Topic.id).limit(30))

    #query = Topic.select().annotate(Post).order_by(Post)
    namen=[]
    namen_id=[]
    count_x=[]
    
    for x in myquery:
        count_x.append(x.count)
        print x.id
        print x.count
        namen_id.append(x.id)
        namen.append(x.name)

    keys = namen
    values = count_x
    adict = dict(itertools.izip(keys,values))

    for x in adict:
        print x

    with open('topic_count_posts.csv', 'wb') as f:
        writer = csv.writer(f)
        for key, value in adict.items():
            writer.writerow([key, value])
   

   
    fig= plt.figure(facecolor="white")
    ax = fig.add_subplot(111, axisbg="white")
    ax.spines["top"].set_visible(False)  
    ax.spines["right"].set_visible(False) 
    ax.get_xaxis().tick_bottom()  
    ax.get_yaxis().tick_left() 
    ax.set_title('Number of Posts per Topic')
    ax.set_xlabel('Topic')
    ax.set_ylabel('Number of Posts')
    index = np.arange(30)
    bar_width = 0.35
    
    t=plt.bar(index, count_x, color="#3F5D7D")
    
    plt.xticks(index + bar_width,namen, rotation=90)
    
    plt.show()
    fig.savefig('topic_posts.png', facecolor=fig.get_facecolor(), edgecolor='none')


def user_count_posts():

   
    
    myquery=(User.select(User.id, User.name, fn.Count(Post.id).alias('count'))).join(Post).naive().group_by(User.id).order_by(fn.Count(Post.id).desc())
    namen=[]
    namen_id=[]
    count_x=[]
    len_q=0
    for x in myquery:
        namen_id.append(x.id)
        namen.append(x.name)
        count_x.append(x.count)
        len_q+=1

    keys = namen
    values = count_x
    adict = dict(itertools.izip(keys,values))

    for x in adict:
        print x

    with open('user_count_posts.csv', 'wb') as f:
        writer = csv.writer(f)
        for key, value in adict.items():
            writer.writerow([key, value])
   

    fig= plt.figure(facecolor="white")
    ax = fig.add_subplot(111, axisbg="white")
    ax.spines["top"].set_visible(False)  
    ax.spines["right"].set_visible(False) 
    
    ax.get_xaxis().tick_bottom()  
    ax.get_yaxis().tick_left() 
    ax.set_title('Number of Posts per User')
    ax.set_xlabel('User')
    ax.set_ylabel('Number of Posts')
    index = np.arange(len_q)
    bar_width = 0.35
    
    t=plt.bar(index, count_x, color="#3F5D7D")
    
    plt.xticks(index + bar_width,namen, rotation=90)
    
    plt.show()
    plt.savefig("test")


