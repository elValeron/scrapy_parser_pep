from collections import defaultdict
import csv

from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session


from pep_parse.models import Base, Pep
from pep_parse.constants import BASE_DIR, STATUS_SUMMARY

class PepParsePipeline:
    statuses = defaultdict(int)

    def open_spider(self, spider):
        engine = create_engine('sqlite:///sqlite.db')
        Base.metadata.create_all(engine)
        self.session = Session(engine)
        
    def process_item(self, item, spider):
        try:    
            pep = Pep(
                number=item['number'],
                name=item['name'],
                status=item['status']
            )
            self.session.merge(pep)
            self.session.commit()
            self.statuses[pep.status] += 1
        except IntegrityError:
            self.session.rollback()
            self.statuses[pep.status] += 1
        return item

    def close_spider(self, spider):
        self.statuses['Total'] = sum(self.statuses.values())
        field_names = ['Status', 'Count']
        print(type(self.statuses))
        with open(STATUS_SUMMARY, 'w', encoding='utf-8') as f:
            
            writer = csv.DictWriter(f=f, fieldnames=field_names)
            writer.writeheader()
            for status, count in self.statuses.items():
                writer.writerow({'Status': status, 'Count': count})
        self.session.close()
