import scrapy

from pspider.items import SiteItem, PostItem

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
            print "fehlerhhttps://www.premium-cola.de/board/viewtopic.php?f=354&t=1230&sid=1a9a300b2b03dd69c16fa0806fb53e07after name"
            return
        else:
            return scrapy.Request(url="https://www.premium-cola.de/board/viewtopic.php?f=354&t=1230",
               callback=self.parse_topicpage)
        # continue scraping with authenticated session...


    
    def parse_topicpage (self, response):
        print "in parse-...."
		
        body=response.xpath('//body').extract()
        
        site=Siteitem()
        site['body']=body
        print site['body']
        topic=response.xpath('//div[@class="panel"]//h2/a/text()').extract()[0]
       
        site['topic']=topic 
        print site['topic']       
        posts=response.xpath('//div[@class="postbody"]')
        for index, post in enumerate(posts):
                
            args=(index, post.xpath('.//p[@class="author"]//a/text()').extract()[0],post.xpath('.//div[@class="content"]/text()').extract(), post.xpath('.//p[@class="author"]/text()').extract()[1])
            
            print "post topic is post number %d is from %s and containts %s and timestamp %s \n \n" % args







       
