# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html




def process_item (self, item, spider):
        
        text=item['post']
        timestamp=item['timestamp']
        order=item['order']
        user=item['user']
        topic=item['topic']
        try:
            post=Post.get(Post.text==text, timestamp==timestamp)

        except Post.DoesNotExist:
            post=Post.create(text=text, timestamp=timestamp, order=order # ja und hier müsste ich aber halt die FKs reingeben!!

        if item['user']:
            # get AUTHOR
				try:
					user=User.get(User.name == item['user'])
				
				# no Author? create one!
				except User.DoesNotExist:
					user = User.create(name = item['user'])
                
        else:
            raise DropItem("No user")
