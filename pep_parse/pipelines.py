from collections import defaultdict
import csv
import datetime as dt

from pep_parse.settings import (BASE_DIR,
                                RESULTS_DIR,
                                STATUS_SUMMARY,
                                DATETIME_FORMAT)


class PepParsePipeline:

    def __init__(self):
        self.results_dir = BASE_DIR / RESULTS_DIR
        self.results_dir.mkdir(exist_ok=True)

    def open_spider(self, spider):
        self.statuses = defaultdict(int)

    def process_item(self, item, spider):
        self.statuses[item['status']] += 1
        return item

    def close_spider(self, spider):
        with open(
            self.results_dir / STATUS_SUMMARY.format(
                time=dt.datetime.now().strftime(DATETIME_FORMAT)
            ),
            'w',
            encoding='utf-8'
        ) as f:
            csv.writer(
                f,
                dialect=csv.unix_dialect,
                quoting=csv.QUOTE_MINIMAL,
            ).writerows(
                [
                    ('Статус', 'Количество'),
                    *self.statuses.items(),
                    ('Total', sum(self.statuses.values()))
                ]
            )
