# coding=utf-8
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.item import Item
from urlparse import urlparse
import os
import re

class YellowPages(CrawlSpider):
    name = 'ypcomvn'
    allowed_domains = ['ellowpages.com.vn']
    
    #start_urls = ['http://www.yellowpages.com.vn/chi-tiet/225255.html']
    counter = 0;

    def start_requests(self):
        for i in range(0, 10):#225255
            url = "http://yellowpages.com.vn/chi-tiet/%s.html" % i
            yield self.make_requests_from_url(url)

    def parse(self, response):
        print "blah blah -------------------"
        if re.search("Hồ Chí Minh", response.body, re.IGNORECASE) is not None:
            self.counter = self.counter + 1
            name = response.url.split("/")[-1]
            open("data/ypcomvn/%s" % name, 'wb').write(response.body)
        
            open("data/ypcomvn/__LOG.dat", "ab").write("%s> %s\n" % (self.counter, name))
        else:
            print "wtf ?"
    
    
    
    
