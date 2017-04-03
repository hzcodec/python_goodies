#!/usr/bin/env python

#   Auther      : Heinz Samuelsson
#   Date        : 2017-03-30
#   File        : fsm5.py
#   Reference   : http://gnosis.cx/publish/programming/charming_python_4.html
#   Description : FSM. cargo can be used as a container for user data.
#                 All state class shall contain:
#                     __init__(), define_states(), go()
#                 Then all states has to be implemented.
#
#   Python ver  : 2.7.3 (gcc 4.6.3)

from time import sleep
import statemachine2 as sm
import events

DLY = 0.5

class Cargo:
    name = ''
    x = 0
    y = 0

class StateMachine_B:
    def __init__(self):
	print 'Create', self.__class__.__name__
        self.m = sm.StateMachine()
	self.define_states()
	self.cargo = Cargo()
        self.EV = events.Events()

    def define_states(self):
        print 'Define states for', self.__class__.__name__
        self.m.add_state("STATE1", self.state1)
        self.m.add_state("STATE2", self.state2)
        self.m.add_state("OUT_OF_RANGE", None, end_state=1)
        self.m.set_start("STATE1")

    def state1(self, cargo):
        self.cargo.x += 1
        self.cargo.y += 4
	self.cargo.name = 'Mattias'
        print "STATE1 State in", self.__class__.__name__ + "  cargo:", self.cargo.x
        newState =  "STATE2";
        sleep(DLY)
        return (newState, self.cargo)
    
    def state2(self, cargo):
        print  "STATE2 State in", self.__class__.__name__ + "  cargo:", self.cargo.x, self.cargo.y, self.cargo.name
        newState =  "STATE1";
	self.EV.SKIP = 1

        if (self.cargo.x == 4):
            print  "Out of range! Quit application. Object:", self.__class__.__name__
            newState =  "OUT_OF_RANGE";
        else:
            newState =  "STATE1";
        sleep(DLY)
        return (newState, self.cargo)
    
    def go(self):
        #print 'go'
	self.m.run(1)


if __name__ == "__main__":

    two = StateMachine_B()
    EV = events.Events()

