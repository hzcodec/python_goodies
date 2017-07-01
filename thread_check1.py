#!/usr/bin/env python

#   Auther      : Heinz Samuelsson
#   Date        : 2017-06-29
#   File        : thread_check1.py
#   Reference   : -
#   Description : Dynamically connect a USB to serial.
#   Python ver  : 2.7.3 (gcc 4.6.3)

import wx
import serial
import os
import time
import sys
from serial.tools import list_ports
import glob
import threading
from wx.lib.pubsub import setupkwargs
from wx.lib.pubsub import pub


class PollPortName(threading.Thread):

    def __init__(self):
        self.portIsConnected = False
        self.portIsDisconnected = False
        self.portIsClosed = False
        self.lock = False 
	self.lock2 = False
	self.sentPortName = 'Connect USB cable'
	self.tmpList = []

        th = threading.Thread.__init__(self)
	self.setDaemon(True)
        self.start()    # start the thread
 
    def run(self):
    
        ser, portName = self.connect_port()

        while True:

	    if (portName == 'No device'):
                self.tmpList = glob.glob('/dev/ttyA*') + glob.glob('/dev/ttyUSB*')

		if not(self.tmpList):
		    pass
		else:
		    portName = self.tmpList[0]

	    # if port exists
	    if (os.path.exists(portName) == True and self.lock == False):
	        self.portIsDisconnected = False
	        self.portIsConnected = True
	        self.lock = True
		self.sentPortName = portName
	        print '\nPort is connected to:', portName 

	    # if port does not exists
	    elif (os.path.exists(portName) == False and self.lock == True):
	        self.portIsDisconnected = True
	        self.portIsConnected = False

	        self.portIsClosed = True # ---
                ser.close()

	        self.lock = False
	        self.lock2 = True
		self.sentPortName = 'Connection lost'
	        print '\nPort is disconnected'

	    # reconnect port
            if (self.portIsConnected == True and self.portIsDisconnected == True):
	        print 'Reconnect: ' + portName
	        time.sleep(1)
	        ser, portName = self.connect_port()
    
            wx.CallAfter(pub.sendMessage, "TOPIC_PORTNAME", msg=self.sentPortName)
	    time.sleep(1)

    def connect_port(self):
        try:
            tempList = glob.glob('/dev/ttyA*') + glob.glob('/dev/ttyUSB*')
	    print 'Read port names:', tempList

            ser = serial.Serial()
            ser.braudrate = 9600
            ser.port = tempList[0]
            ser.open()

        except:
            print 'No connection'
	    tempList.append('No device')
            #sys.exit()

        if ser.isOpen():
            print("Serial port is open")

        return ser, tempList[0]


class Example(wx.Frame):
  
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(260, 180))

        pub.subscribe(self.get_port_name, "TOPIC_PORTNAME")

	self.txtInfo = wx.StaticText(self, wx.ID_ANY, 'No connection established yet')

        self.InitUI()
        self.Centre()
        self.Show()

    def InitUI(self):
    
        menubar = wx.MenuBar()
        filem = wx.Menu()

        menubar.Append(filem, '&File')
        self.SetMenuBar(menubar)

	self.btnConnect = wx.Button(self, wx.ID_ANY, 'Connect', pos=(10, 50))
	self.Bind(wx.EVT_BUTTON, self.onConnect, self.btnConnect)


    def get_port_name(self, msg):

        #print 'Rec msg:', msg
	if (msg == 'Connection lost'):
	    #self.btnConnect.Enable(True)
	    pass

	self.txtInfo.SetLabel(msg)

    def onConnect(self, event):
	PollPortName()
	#self.btnConnect.Enable(False)


if __name__ == '__main__':
  
    app = wx.App()
    Example(None, title='')
    app.MainLoop()

