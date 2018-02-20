# Author      : Heinz Samuelsson
# Date        : Fri Mar 25 10:38:15 CET 2016
# File        : context1.py
# Reference   : https://www.youtube.com/watch?v=-aKFBoZpiqA 
# Description : Example of how to use context manager when opening a file.
#               A file 'sample.txt' is created.
#
#               This is just an example of how a context manager is working.
#               Open file handling is already handled within Python's context manager.
#
# Python ver  : Python 3.5.2 (default, Nov 23 2017, 16:37:01) 

class Open_File():

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, traceback):
        self.file.close()


with Open_File('sample.txt', 'w') as f:
    f.write('Hello There')

print(f.closed)
