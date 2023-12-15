import datetime as dt
from pathlib import Path

BASE_DIR = Path(__file__).parent
RESULTS_DIR = BASE_DIR / 'results'
PEP_INFO = 'pep_%(time)s.csv'
STATUS_SUMMARY = RESULTS_DIR / 'status_summary_{time}.csv'.format(time=dt.datetime.now())
