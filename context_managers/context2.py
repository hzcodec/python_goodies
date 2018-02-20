# Author      : Heinz Samuelsson
# Date        : Fri Mar 25 10:38:15 CET 2016
# File        : context2.py
# Reference   : https://www.youtube.com/watch?v=-aKFBoZpiqA 
# Description : Example of how to use context manager with a decorator.
#               A file 'sample2.txt' is created.
#
# Python ver  : Python 3.5.2 (default, Nov 23 2017, 16:37:01) 

from contextlib import contextmanager


@contextmanager
def open_file(file, mode):
    
    try:
        f = open(file, mode)
        yield f
  
    finally:
        f.close()

with open_file('sample2.txt', 'w') as f:
    f.write('Jennie Samuelsson')


print(f.closed)
