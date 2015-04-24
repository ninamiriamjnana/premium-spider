import scrapy

from pspider.items import PostItem

class LoginSpider(scrapy.Spider):
    name = 'premium_login'
    start_urls = ['https://www.premium-cola.de/board/ucp.php?mode=login']

    
    def __init__(self, username="", password="", *args, **kwargs):
    	super(LoginSpider, self).__init__(*args, **kwargs)
    	self.username = username
        self.password=password
	
     

    def parse(self, response):
        return [scrapy.FormRequest.from_response(response,
                    formdata={'username': self.username, 'password': self.password},
                    callback=self.after_login)]

    def after_login(self, response):
        # check login succeed before going on
        if "Du hast ein fehlerhaftes Passwort angegeben" in response.body:
            print "fehlerhaftes passwort"
            return
        if "Du hast einen fehlerhaften Benutzernamen angegeben" in response.body:
            print "fehler after name"
            return
        else:
            return scrapy.Request(url="https://www.premium-cola.de/board/viewtopic.php?f=354&t=1230",
               callback=self.parse_topicpage)
        # continue scraping with authenticated session...


    
    def parse_topicpage (self, response):
        print "in parse-...."
		
        body=response.xpath('//body').extract()
        
        url=response.url
       
        topic=response.xpath('//div[@class="panel"]//h2/a/text()').extract()[0]
       
         
        posts=response.xpath('//div[@class="postbody"]')
        for index, post in enumerate(posts):
                
            save_post=PostItem()
            save_post["user"]=post.xpath('.//p[@class="author"]//a/text()').extract()[0]
            save_post["order"]=index
            save_post["text"]=post.xpath('.//div[@class="content"]/text()').extract() # das hier ist eine liste. musss einen string draus machen
            save_post["text"]="".join(save_post["text"])
            save_post["timestamp"]=post.xpath('.//p[@class="author"]/text()').extract()[1]
            save_post["topic"]=topic
            save_post["body"]=body
            save_post["url"]=url
            print ("post topic is numer %d is from %s and contains %s and timestamp %s and topic %s" % (save_post["order"], save_post["user"], save_post["text"], save_post["timestamp"], save_post["topic"]))
            yield save_post







       
