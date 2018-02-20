# Author      : Heinz Samuelsson
# Date        : Fri Mar 25 10:38:15 CET 2016
# File        : context4.py
# Reference   : https://stackoverflow.com/questions/3693771/trying-to-understand-python-with-statement-and-context-managers
# Description : -
#
# Python ver  : Python 3.5.2 (default, Nov 23 2017, 16:37:01) 

class Door:

     # allocation of the class
     def __init__(self):
         self.doorstatus = 'The door was closed when you are not home'
         print(self.doorstatus)

     # entering the context
     def __enter__(self):
         print('I have opened the door')
         return self

     # exit the context
     def __exit__(self,*args):
         print('Pong! The door has been closed')

     def fetchsomethings(self):
         print('I fetched somethings')


with Door() as dr:
    dr.fetchsomethings()
