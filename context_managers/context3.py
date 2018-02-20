# Author      : Heinz Samuelsson
# Date        : Fri Mar 25 10:38:15 CET 2016
# File        : context3.py
# Reference   : https://www.youtube.com/watch?v=-aKFBoZpiqA 
# Description : Another example of how to use context manager with a decorator.
#
# Python ver  : Python 3.5.2 (default, Nov 23 2017, 16:37:01) 

import os
from contextlib import contextmanager


@contextmanager
def change_dir(destination):
    try:
        cwd = os.getcwd()
        os.chdir(destination)
        yield

    finally:
        os.chdir(cwd)
        

# Now we can reuse this context manager over and over again.
# All resources will be managed as we want.
with change_dir('Sample-Dir-One'):
    print(os.listdir())

with change_dir('Sample-Dir-Two'):
    print(os.listdir())

