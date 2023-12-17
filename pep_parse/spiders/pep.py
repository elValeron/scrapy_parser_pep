import re

import scrapy

from pep_parse.constants import START_URL, ALLOWED_DOMAINS
from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ALLOWED_DOMAINS
    start_urls = START_URL

    def parse(self, response):
        pep_all = response.css('#numerical-index tbody a')
        for pep in pep_all:
            yield response.follow(pep, callback=self.parse_pep)

    def parse_pep(self, response):
        number_name = response.xpath(
            '//article//h1[@class="page-title"]//text()'
        ).getall()
        pattern = r'PEP\s(?P<number>(\d+)) – (?P<name>(.+))'
        string = re.search(pattern=pattern, string=''.join(number_name))
        yield PepParseItem(
            number=int(string.group('number')),
            name=string.group('name'),
            status=response.css('abbr::text').get()
        )
