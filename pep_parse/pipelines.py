from collections import defaultdict
import csv
import datetime as dt

from pep_parse.settings import (BASE_DIR,
                                RESULTS_DIR,
                                STATUS_SUMMARY,
                                DATETIME_FORMAT)


class PepParsePipeline:
    def __init__(
            self,
            statuses=defaultdict(int),
            statistic={}
            ):
        self.statuses = statuses
        self.statistic = statistic

    def process_item(self, item, spider):
        self.pep_information = {
            'number': item['number'],
            'name': item['name'],
            'status': item['status']
        }
        self.statuses[item['status']] += 1
        return item

    def close_spider(self, spider):
        self.statuses['Total'] = sum(self.statuses.values())
        field_names = ['Status', 'Count']
        with open(
            BASE_DIR / RESULTS_DIR / STATUS_SUMMARY.format(
                time=dt.datetime.now().strftime(DATETIME_FORMAT)
            ),
            'w',
            encoding='utf-8'
        ) as f:
            writer = csv.DictWriter(
                f=f,
                fieldnames=field_names,
                delimiter=','
            )
            writer.writeheader()
            for status, count in self.statuses.items():
                writer.writerow({'Status': status, 'Count': count})
