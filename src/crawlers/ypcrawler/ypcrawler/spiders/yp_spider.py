# coding=latin-1
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.item import Item
from urlparse import urlparse
import os
import re

class YellowPageSpider(CrawlSpider):
    name = 'dmoz'
    allowed_domains = ['yellowpages.vnn.vn']
    start_urls = ['http://yellowpages.vnn.vn/business/Category_listings.asp?classcode=89400&town_id=54&keyword=&keywordunsign=&nganhnghe=&searchfor=&loc=D']

    rules = (
        # Extract links matching 'category.php' (but not matching 'subsection.php')
        # and follow links from them (since no callback means follow=True by default).
        Rule(SgmlLinkExtractor(allow=('yellowpages.vnn.vn/business/Category_listings.asp.*$', ))),

		
        # Extract links matching 'item.php' and parse them with the spider's method parse_item
        Rule(SgmlLinkExtractor(allow=('yellowpages.vnn.vn/business/listings_detail.asp.*$', )), callback='parse_item'),
    )

    def parse_item(self, response):
		if re.search(u"H&#7891; Chí Minh", response.body, re.IGNORECASE) is not None:
			url = urlparse(response.url)
			params = dict([part.split('=') for part in url[4].split('&')])
			filename = os.path.join('data', params['sql_code'])
			open(filename, 'wb').write(response.body)