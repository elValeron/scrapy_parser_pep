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

    def statuses_count(self, statuses=None):
        self.statuses = defaultdict(int) if statuses is None else statuses

    def open_spider(self, spider):
        self.statuses_count()

    def process_item(self, item, spider):
        self.statuses[item['status']] += 1
        return item

    def close_spider(self, spider):
        self.statuses['Total'] = sum(self.statuses.values())
        field_names = ['status', 'count']
        with open(
            self.results_dir / STATUS_SUMMARY.format(
                time=dt.datetime.now().strftime(DATETIME_FORMAT)
            ),
            'w',
            encoding='utf-8'
        ) as f:
            csv.DictWriter(
                f=f,
                fieldnames=field_names,
                dialect=csv.unix_dialect,
                quoting=csv.QUOTE_MINIMAL,
            ).writerows(
                [
                    {'status': status, 'count': count}
                    for status, count in self.statuses.items()
                ]
            )
