# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from peeweemodels import *
from scrapy.exceptions import DropItem
from scrapy.http import Request



class PeeweePipeline(object):
    def process_item (self, item, spider):
            
        text=item['post']
        timestamp=item['timestamp']
        order=item['order']
        user=item['user']
        topic=item['topic']

       # als allererstes speicher ich die html seite
      #get HTMLSite
        try:
            htmlsite=HTMLSite.get(HTMLSite.body == item['body'])
				
	    # no HTMLSite? create one!
	    except HTMLSite.DoesNotExist:
	        htmlsite= HTMLSite.create(body = item['body'])  

       # ich fang mit denen an, von denen ich nachher die FKs brauche: topic und user  
       # danach schreib ich alles andere rein
            
            
            if item['user']:
                # get USER
				    try:
					    user=User.get(User.name == item['user'])
				
				    # no USER? create one!
				    except User.DoesNotExist:
					    user = User.create(name = item['user'])
                if item['topic']:
                    # get TOPIC
				    try:
					    topic=Topic.get(Topic.name == item['topic'])
				
				    # no Topic? create one!
				    except Topic.DoesNotExist:
					    topic= Topic.create(name = itemitem['topic'])
                  
                     try:
                        post=Post.get(Post.text==text, timestamp==timestamp)

                    except Post.DoesNotExist:
                        post=Post.create(text=text, timestamp=timestamp, order=order, topic=topic, user=user) #

                      
                else:
                    raise DropItem("No topic")
                    
            else:
                raise DropItem("No user")

         return item

       
       
        
