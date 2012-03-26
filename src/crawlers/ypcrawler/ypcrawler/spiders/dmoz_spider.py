# coding=latin-1
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.item import Item
from urlparse import urlparse
import os
import re

class DmozSpider(CrawlSpider):
    name = 'dmoz'
    allowed_domains = ['diadiem.com']
    start_urls = ['http://www.diadiem.com/directory.aspx?st=SaiGon&l=0']

    rules = (
        # Extract links matching 'category.php' (but not matching 'subsection.php')
        # and follow links from them (since no callback means follow=True by default).
        Rule(SgmlLinkExtractor(allow=('diadiem.com/directory.aspx.*$', ))),

		
        # Extract links matching 'item.php' and parse them with the spider's method parse_item
        Rule(SgmlLinkExtractor(allow=('diadiem.com/Result.aspx.*$', )), callback='parse_item'),
    )

    def parse_item(self, response):
		print response.url