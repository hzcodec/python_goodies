# Author      : Heinz Samuelsson
# Date        : Fri Mar 25 10:38:15 CET 2016
# File        : class_context1.py
# Reference   : https://pymotw.com/2/contextlib/
# Description : - 
# Python ver  : Python 2.7

class WithinContext(object):

    def __init__(self, context):
        print 'WithinContext.__init__(%s)' % context
        
    def do_something(self):
        print 'WithinContext.do_something()\n'

    def __del__(self):
        print 'WithinContext.__del__'
        

class Context(object):

    def __init__(self):
        print 'Context.__init__()'

    def __enter__(self):
        print 'Context.__enter__()\n'
        return WithinContext(self)

    def __exit__(self, exc_type, exc_val, exc_tb):
        print 'Context.__exit__()\n'
    

with Context() as c:
    c.do_something()
