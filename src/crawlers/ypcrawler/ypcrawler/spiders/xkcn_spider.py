from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor

class xkcnSpider(CrawlSpider):
    name = "xkcn"
    allowed_domains = ["xkcn.info"]
    start_urls = [
        "http://xkcn.info"
    ]
    rules = (
        # Extract links matching 'category.php' (but not matching 'subsection.php')
        # and follow links from them (since no callback means follow=True by default).
        Rule(SgmlLinkExtractor(allow=('xkcn.info/page/*$', ))),
    )

    def parse(self, response):
        filename = response.url.split("/")[-2]
        open(filename, 'wb').write(response.body)