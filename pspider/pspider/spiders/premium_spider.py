import scrapy

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

from pspider.items import PostItem

class LoginSpider(CrawlSpider):
    name = 'premium_login'
    login_page='https://www.premium-cola.de/board/ucp.php?mode=login'
    allowed_domains=['premium-cola.de']
    start_urls=['https://www.premium-cola.de/board/index.php?sid=d1b48640148a07ebceb8df77d8087c35']

    rules = (
         # Extract links matching 'category.php' (but not matching 'subsection.php')
        # and follow links from them (since no callback means follow=True by default).
        Rule(LinkExtractor(allow=('/board/viewforum.php\?f=306', ))),
       

        # Extract links matching 'item.php' and parse them with the spider's method parse_item
        Rule(LinkExtractor(allow=(r'/board/viewforum.php\?f=[0-9]+\&t=[0-9]+', )), callback='parse_topicpage'),
    )
        


    def start_requests(self):
    yield Request(
    url=self.login_page,
    callback=self.login,
    dont_filter=True
    )
	
    def login(self, response):
    #"""Generate a login request."""
    return FormRequest.from_response(response,
            formdata={'username': self.username, 'password': self.password},
            callback=self.check_login_response)     

   
    

    def check_login_response(self, response):
        # check login succeed before going on
        if "Du hast ein fehlerhaftes Passwort angegeben" in response.body:
            print "fehlerhaftes passwort"
            return
        if "Du hast einen fehlerhaften Benutzernamen angegeben" in response.body:
            print "fehler after name"
            return
        else:
            return Request(url="https://www.premium-cola.de/board/index.php?sid=d1b48640148a07ebceb8df77d8087c35")
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







       
