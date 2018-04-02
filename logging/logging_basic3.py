import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(levelname)s : %(funcName)s() - %(message)s')

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(stream_handler)


def add(a, b):
    logger.info('Add called, a={}, b={}'.format(a, b))
    return a+b

def sub(a, b):
    logger.info('Sub called, a={}, b={}'.format(a, b))
    return a-b

def div(a, b):
    if b == 0:
        logger.error('Houston we got a problem, b={}'.format(b))
    else:
        return a-b


n1 = 17
n2 = 27

add_result = add(n1, n2)
sub_result = sub(n1, n2)
div_result = div(n1, 0)

