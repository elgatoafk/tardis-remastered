import logging
import os
from datetime import datetime

log_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'logs')
os.makedirs(log_dir, exist_ok=True)

current_date = datetime.now().strftime('%Y-%m-%d')
log_filename = os.path.join(log_dir, f'{current_date}.log')

logging.basicConfig(
    filename='time_conversion.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)