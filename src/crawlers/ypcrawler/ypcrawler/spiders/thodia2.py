# coding=latin-1
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.item import Item
from urlparse import urlparse
import os
import re
from scrapy.http.request.form import FormRequest
from scrapy.http.request import Request
import urllib2,urllib
from BeautifulSoup import BeautifulSoup

class thodiaSpider2(CrawlSpider):
    counter = 0
    pcounter = 0
    name = 'thodia2'
    allowed_domains = ['thodia.vn']
    start_urls = ['http://thodia.vn/websites/SearchResult.aspx?loNameID=&lo=hcm']
    #http://thodia.vn/websites/SearchResult.aspx?loNameID=&lo=hcm 51862
    #http://thodia.vn/Websites/SearchResultHotspot.aspx?locationID=1&CategoryID=0&kd=101
    rules = (
        #http://thodia.vn/Websites/SearchResultHotspot.aspx?locationID=1&CategoryID=1&hpcateid=f0250562-c587-4976-a52d-b84db5a23ae8
        #Rule(SgmlLinkExtractor(allow=('http://thodia.vn/Websites/SearchResultHotspot.aspx.*$', ))),

        
        # Rule(SgmlLinkExtractor(allow=('http://thodia.vn/([a-z-]*)ho-chi-minh(-[0-9])?.html', )), callback='parse_item'),
    )
    
    
    def parseOne(self, response, i):
        return FormRequest.from_response(response,
                    formdata={'__EVENTTARGET': 'ctl00$ContentPlaceHolder1$ucPaging$repPages$ctl%s$lkbPage'%i, 
                              '__EVENTARGUMENT': '',
                              'ctl00$ContentPlaceHolder1$hdfPage': '%s'%i},
                    callback=self.callback_now)
    
    def parse(self, response):
        #return [self.parseOne(response, 100)]
        urls = []
        total = 51862
        npage = 5187 #npage + 1
        for i in range(1, 4):
            urls.append(self.parseOne(response, i))
            
        return urls
    
    def callback_now(self, response):
        self.pcounter += 1
        open("data/thodia/page/%s.html" % self.pcounter, "wb").write(response.body)
        
        hxs = HtmlXPathSelector(response)
        
        for url in hxs.select('//div[@id="HotspotResult_Info"]/div/a[@class="LinkGreen"]/@href').extract():
            yield Request(url, callback=self.parse_item)
    
    def parse_item2(self, response):
        print response.url

    def parse_item(self, response):
        self.counter += 1
        name = response.url.split("/")[-1]
        print ""
        print "> ", name
        print ""
        

        soup = BeautifulSoup(response.body)
        
        for script in soup("script"):
            script.extract()
        
        with open("data/thodia/%s" % name, "w") as f:
            f.write(soup.prettify())

        open("data/thodia/__LOG.dat", "ab").write("%s> %s\n" % (self.counter, name))
    
    
    
    
