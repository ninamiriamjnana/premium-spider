import scrapy


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
            print "fehlerhafter name"
            return
        else:
            return scrapy.Request(url="https://www.premium-cola.de/board/viewtopic.php?f=354&t=1230",
               callback=self.parse_topicpage)
        # continue scraping with authenticated session...


    
    def parse_topicpage (self, response):
        print "in parse-...."
        
        posts=response.xpath('//div[@class="postbody"]')
        for index, post in enumerate(posts):
            args=(index, post.xpath('.//a[@class="username-coloured"]/text()').extract(),post.xpath('.//div[@class="content"]/text()').extract())
            print "post number %d is from %s and containts %s \n \n" % args







       
