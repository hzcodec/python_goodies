#!/usr/bin/env python

#   Auther      : Heinz Samuelsson
#   Date        : 2017-03-30
#   File        : statemachine2.py
#   Reference   : http://gnosis.cx/publish/programming/charming_python_4.html
#   Description : FSM
#   Python ver  : 2.7.3 (gcc 4.6.3)

import sys
from string import upper

class StateMachine:
    def __init__(self):
        self.handlers = {}
        self.startState = None
        self.endStates = []
	self.handler = None
	self.cargo = 0

    def add_state(self, name, hdlr, end_state=0):
        name = upper(name)
        self.handlers[name] = hdlr

        if end_state:
             self.endStates.append(name)

	#print 'Add:', self.handlers

    def set_start(self, name):
        self.startState = name
        self.handler = self.handlers[self.startState]

    def run(self, cargo):
        newState, self.cargo = self.handler(self.cargo)

        if newState in self.endStates:
            sys.exit()

        self.handler = self.handlers[newState]
	#print 'newState', newState


