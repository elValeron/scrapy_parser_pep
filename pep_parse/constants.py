from pathlib import Path

"""PATH"""
BASE_DIR = Path(__file__).parent.parent
RESULTS_DIR = 'results'
ENGINE_PATH = 'sqlite:///sqlite.db'

"""FILENAMES"""
STATUS_SUMMARY = 'status_summary_{time}.csv'
PEP_INFO = 'pep_%(time)s.csv'

"""FORMAT"""
DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'

"""URLS"""
START_URL = ['https://peps.python.org/']
ALLOWED_DOMAINS = ['peps.python.org']
