# Author      : Heinz Samuelsson
# Date        : Fri Mar 25 10:38:15 CET 2016
# File        : context5.py
# Reference   : -
# Description : -
#
# Python ver  : Python 3.5.2 (default, Nov 23 2017, 16:37:01) 

from contextlib import ContextDecorator

class Door(ContextDecorator):

     def __enter__(self):
         self.doorstatus = 'The door is closed when you are not home'
         print(self.doorstatus)

     def __exit__(self, *exc):
         print('I have opened the door')


@Door()
def do_door():
    print('Hello! Open the door')


do_door()
