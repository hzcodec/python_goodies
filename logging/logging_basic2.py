import logging
import Employee

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
file_handler = logging.FileHandler('sample.log')
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)


def add(a, b):
    logger.error('I got an Error')
    return a+b

def sub(a, b):
    return a-b


n1 = 17
n2 = 27

add_result = add(n1, n2)
logger.info('Add {} + {} = {}'.format(n1, n2, add_result))

sub_result = sub(n1, n2)
logger.info('Sub {} - {} = {}'.format(n1, n2, add_result))

