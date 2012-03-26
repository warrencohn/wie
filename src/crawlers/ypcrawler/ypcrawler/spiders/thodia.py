# coding=latin-1
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.item import Item
from urlparse import urlparse
import os
import re
from scrapy.http.request.form import FormRequest

class thodiaSpider(CrawlSpider):
    name = 'thodia'
    allowed_domains = ['thodia.vn']
    # start_urls = ['http://thodia.vn/hcm']

    rules = (
        # Extract links matching 'category.php' (but not matching 'subsection.php')
        # and follow links from them (since no callback means follow=True by default).
        Rule(SgmlLinkExtractor(allow=('http://thodia.vn/([a-z-]*)$', ))),
        
        Rule(SgmlLinkExtractor(allow=('http://thodia.vn/Websites/SearchResultHotspot.aspx?.*$', ))),

        
        # Extract links matching 'item.php' and parse them with the spider's method parse_item
        Rule(SgmlLinkExtractor(allow=('http://thodia.vn/([a-z-]*)ho-chi-minh(-[0-9])*.html', )), callback='parse_item'),
    )
    
    def start_requests(self):
        return [FormRequest("http://thodia.vn/hcm", 
                            formdata={'__EVENTTARGET':'ctl00$lbtHCM'},
                callback=self.set_location)]
    
    def set_location(self, response):
        print "started !"
        pass

    def parse_item(self, response):
        print response.url
        pass
    
    
    
    
