import logging
# default logging is warning
# DEBUG
# INFO
# WARNING
# ERROR


logging.basicConfig(level=logging.DEBUG)

def add(a, b):
    return a+b

def sub(a, b):
    return a-b


n1 = 10
n2 = 20

add_result = add(n1, n2)
logging.debug('Add {} + {} = {}'.format(n1, n2, add_result))

sub_result = sub(n1, n2)
logging.debug('Sub {} - {} = {}'.format(n1, n2, add_result))
logging.info('Hello')

