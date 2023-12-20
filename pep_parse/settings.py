from pathlib import Path

"""PATH"""
BASE_DIR = Path(__file__).parent.parent
RESULTS_DIR = 'results'

"""FILENAMES"""
STATUS_SUMMARY = 'status_summary_{time}.csv'
PEP_INFO = 'pep_%(time)s.csv'

"""FORMAT"""
DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'

"""URLS"""
ALLOWED_DOMAINS = ['peps.python.org']


BOT_NAME = 'pep_parse'

NEWSPIDER_MODULE = 'pep_parse.spiders'
SPIDER_MODULES = NEWSPIDER_MODULE.split(',')


ROBOTSTXT_OBEY = True

FEEDS = {
    f'{RESULTS_DIR}/{PEP_INFO}': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    }
}
ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}
