# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from peewee import *
from peeweemodels import *
from scrapy.exceptions import DropItem
from scrapy.http import Request



class PeeweePipeline(object):

    def __init__(self):
        self.ids_seen = set()
    

    def process_item (self, item, spider):
        value_id=item['pid']
        if item['pid'] in self.ids_seen:
            raise DropItem("Duplicate item found")
        else:
            self.ids_seen.add(item['pid'])
            
            text=item['text']
            timestamp=item['timestamp']
            order=item['order']
            user=item['user']
            topic=item['topic']
            body=item['body']
            url=item['url']
            pid=item['pid']
            # als allererstes speicher ich die html seite
            #get HTMLSite
            try:
                htmlpage=HTMLPage.get(HTMLPage.url == url)
				
	        # no HTMLSite? create one!
            except HTMLPage.DoesNotExist:

	            htmlpage= HTMLPage.create(body=body, url=url)  

            # ich fang mit denen an, von denen ich nachher die FKs brauche: topic und user  
            # danach schreib ich alles andere rein**/"""
                
                
            if not item['user']:
                raise DropItem("No user")
            else:
                # get USER
                try:
			        user=User.get(User.name == item['user'])
		
		        # no USER? create one!
                except User.DoesNotExist:
                    user = User.create(name = item['user'])
                if not item['topic']:
                    raise DropItem("No topic")
                else:
                    # get TOPIC
                    try:
                        topic=Topic.get(Topic.name == item['topic'])
                    except Topic.DoesNotExist:
                        topic= Topic.create(name = item['topic'])
                    try:
                        post=Post.get(Post.pid==pid)

                    except Post.DoesNotExist:
                        post=Post.create(text=text, timestamp=timestamp, order=order, topic=topic, user=user, pid=pid) 

              
                    
                    
           
                

            return item

       
       
        
