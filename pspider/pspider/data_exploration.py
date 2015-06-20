from peeweemodels import *

import matplotlib.pyplot as plt

from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})

import numpy as np



def user_and_topic():
    myquery=(User.select(User.id, User.name,Topic.name.alias('topic_name')).join(Post).join(Topic).naive().order_by(Topic.id))
    for x in myquery:
        x.name
        x.topic_name

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
    for x in myquery:
        namen_id.append(x.id)
        namen.append(x.name)
        count_x.append(x.count)

    fig= plt.figure(facecolor="white")
    ax = fig.add_subplot(111, axisbg="white")
    ax.spines["top"].set_visible(False)  
    ax.spines["right"].set_visible(False) 
    
    ax.get_xaxis().tick_bottom()  
    ax.get_yaxis().tick_left() 
    ax.set_title('Number of Posts per User')
    ax.set_xlabel('User')
    ax.set_ylabel('Number of Posts')
    index = np.arange(44)
    bar_width = 0.35
    
    t=plt.bar(index, count_x, color="#3F5D7D")
    
    plt.xticks(index + bar_width,namen, rotation=90)
    
    plt.show()
    plt.savefig("test")


