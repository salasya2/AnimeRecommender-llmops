import os
import logging
import datetime

LOGS_DIR = 'logs'

os.makedirs(LOGS_DIR, exist_ok = True)

LOGFILE = os.path.join(LOGS_DIR, f"log_{datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.log")

logging.basicConfig(
    filename= LOGFILE,
    format = '%(asctime)s -%(levelname)s - %(message)s',
    level = logging.INFO
)

def get_logger(name):

    logger = logging.getLogger(name)

    logger.setLevel(logging.INFO)

    return logger



