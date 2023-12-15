import re 

import scrapy

from pep_parse.items import PepParseItem

class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        pep_all = response.css('#numerical-index tbody a')
        count = 0
        for pep in pep_all:
            count += 1
            yield response.follow(pep, callback=self.parse_pep)
            if count == 20:
                break

    def parse_pep(self, response):
        number_name = response.css('article h1.page-title::text').get().strip()
        pattern = r'PEP\s(?P<number>(\d+)) – (?P<name>(.+))'
        string = re.search(pattern=pattern, string=number_name)
        yield PepParseItem(
            number=int(string.group(1)),
            name=string.group(3),
            status=response.css('abbr::text').get()
        )