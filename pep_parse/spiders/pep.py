import re

import scrapy

from pep_parse.items import PepParseItem
from pep_parse.settings import ALLOWED_DOMAINS


class PepSpider(scrapy.Spider):

    name = 'pep'
    allowed_domains = ALLOWED_DOMAINS
    start_urls = [f'https://{url}/' for url in ALLOWED_DOMAINS]

    def parse(self, response):
        pep_all = response.css('#numerical-index tbody a')
        for pep in pep_all:
            yield response.follow(pep, callback=self.parse_pep)

    def parse_pep(self, response):
        number_name = response.css(
            'h1.page-title *::text'
        ).getall()
        pattern = r'PEP\s(?P<number>(\d+)) – (?P<name>(.+))'
        string = re.search(pattern=pattern, string=''.join(number_name))
        yield PepParseItem(
            number=string.group('number'),
            name=string.group('name'),
            status=response.css('abbr::text').get()
        )
