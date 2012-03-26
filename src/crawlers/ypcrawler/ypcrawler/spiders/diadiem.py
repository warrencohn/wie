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

class diadiemSpider(CrawlSpider):
    total_dist = 0
    
    name = 'diadiem'
    allowed_domains = ['diadiem.com']
    start_urls = ['http://www.diadiem.com/directory.aspx?st=SaiGon&l=0']

    rules = (
        Rule(SgmlLinkExtractor(allow=('diadiem.com/directory.aspx?.*$', )), ),
        
        Rule(SgmlLinkExtractor(allow=('diadiem.com/Result.aspx\?xy=.*$', )), callback='parse_district'),
    )
    
    def post_json(self, key):
        
        pass
    
    def requestd(self, dist, npage, nrow):
        formdata={'stpe':'3',
                  'st':'SaiGon',
                  'F':'',
                  'C':'',
                  'K':'',
                  'A':dist,
                  'S':'T',
                  'P':npage,
                  'R':nrow,
                  'fD':'1',
                  'uID':'0',
                  'cID':'01',
                  'dID':'0',
                  '_':''
                  }
        
        data = json.load(urllib2.urlopen("http://www.diadiem.com/Comp.aspx", urllib.urlencode(formdata)))
        return data
    
    def get_total_row(self, dist):
        data = self.requestd(dist, '1', '1')
        print "total row %s" % data['tr']
        return data['tr']
    
    def parse_district(self, response):
        url = response.url
        # print url
        
        dist = re.search(r'&xy=.*$', url, re.M|re.I) # scrapy auto sort all parameters of url
        if dist:
            dist_key = dist.group().replace('&xy=', '')
            self.total_dist += 1
            print dist_key
            print type(dist_key)
            self.get_total_row(dist_key)
            
        else:
            print "No match"
    
    
    
    
