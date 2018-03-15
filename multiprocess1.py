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
import wx

port = None


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
            port = self.portList[0] 

            if self.portList:
                self.gotPort = True
	        print 'Get attached ports: %s, gotPort=%d' % (self.portList, self.gotPort)
            else:
                print 'No port available'

            time.sleep(1)

    def stop_worker(self):
        print 'worker 1 is terminated'
        self.portScanner.terminate()


class Example(wx.Frame):
  
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(260, 180))

	self.txtInfo = wx.StaticText(self, wx.ID_ANY, 'No connection established yet')

        self.InitUI()
        self.Centre()
        self.Show()

    def InitUI(self):
    
	self.btnConnect = wx.Button(self, wx.ID_ANY, 'Connect', pos=(10, 50))
	self.Bind(wx.EVT_BUTTON, self.onConnect, self.btnConnect)

    def onConnect(self, event):
	poll_port = PollPort()
        poll_port.start_worker()


if __name__ == '__main__':
  
    app = wx.App()
    Example(None, title='')
    app.MainLoop()

