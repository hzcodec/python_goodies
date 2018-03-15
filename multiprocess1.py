#!/usr/bin/env python

#   Auther      : Heinz Samuelsson
#   Date        : 2018-03-14
#   File        : multiprocess1.py
#   Reference   : -
#   Description : Dynamically connect a USB to serial.
#   Python ver  : 2.7.3 (gcc 4.6.3)

import multiprocessing
import time
import glob
import os

class PollPort():

    def __init__(self):
        print '__init__'
        self.portList = []
        self.gotPort = False

    def start_worker(self):
        print 'Start worker 1'
        self.portScanner = multiprocessing.Process(name='worker 1', target=self.worker)
        self.portScanner.start()

    def worker(self):
        processName = multiprocessing.current_process().name

        while(True):

            self.portList = glob.glob('/dev/ttyA*') + glob.glob('/dev/ttyUSB*')
            print self.portList

            # check if there are any active ports
            if self.portList:
                self.gotPort = True
	        print 'Get attached ports: %s, gotPort=%d' % (self.portList, self.gotPort)
            else:
                print 'No port available'

            time.sleep(1)
            print '---'

    def stop_worker(self):
        print 'worker 1 is terminated'
        self.portScanner.terminate()


if __name__ == '__main__':

    poll_port = PollPort()
    poll_port.start_worker()
    time.sleep(4)

    while (True):
        time.sleep(3)

    print 'Done'

