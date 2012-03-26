# coding=latin-1
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.item import Item
from urlparse import urlparse
import os
import re
import json
import urllib2
import urllib
import pymongo

class diadiemSpider2(CrawlSpider):
    totalResults = 0
    catResult = []
    
    name = 'diadiem2'
    allowed_domains = ['diadiem.com']
    # start_urls = ['http://www.diadiem.com/directory.aspx?st=SaiGon&l=0']

    rules = (
        #Rule(SgmlLinkExtractor(allow=('diadiem.com/directory.aspx?.*$', ))),
        
        Rule(SgmlLinkExtractor(allow=('diadiem.com/directory.aspx.*$', )), callback='parse_cate'),
    )
    
    def post_json(self, key):
        
        pass
    
    def start_requests(self):
        for i in range(1, 28):
            tr = int(self.get_total_row(i))
            self.totalResults += tr 
            self.catResult.append(tr)
        print self.catResult
        print "totalResults %s" % self.totalResults
        
    def requestd(self, cid, npage, nrow):
        formdata={'stpe':'28',
                  'st':'SaiGon',
                  'F':'',
                  'C':'',
                  'K':'',
                  'A':'',
                  'S':'T',
                  'P':npage,
                  'R':nrow,
                  'fD':'1',
                  'uID':'0',
                  'cID':cid,
                  'dID':'0',
                  '_':''
                  }
        
        data = json.load(urllib2.urlopen("http://www.diadiem.com/Comp.aspx", urllib.urlencode(formdata)))
        return data
    
    def get_total_row(self, cate):
        data = self.requestd(cate, '1', '1')
        print "total row %s" % data['tr']
        return data['tr']
    
    def parse_cate(self, response):
        url = response.url
        
 

    def connectDB(self):
        conn = pymongo.Connection()
        db = conn.crawl.diadiem
        
    
    
    
