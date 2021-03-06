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
import fsm6

DLY = 0.2

class Cargo:
    name = ''
    x = 0
    y = 0


class StateMachine_A:
    def __init__(self):
	print 'Create', self.__class__.__name__
        self.m = sm.StateMachine()
	self.define_states()

	# declare an object to hold data
	self.cargo = Cargo()

    def define_states(self):
        print 'Define states for', self.__class__.__name__
        self.m.add_state("STATE1", self.state1)
        self.m.add_state("STATE2", self.state2)
        self.m.add_state("STATE3", self.state3)
        self.m.add_state("OUT_OF_RANGE", None, end_state=1)
        self.m.set_start("STATE1")

    def state1(self, cargo):
        self.cargo.x += 1
	self.cargo.y += 2
	self.cargo.name = 'Jennie'
        print "STATE1 State in", self.__class__.__name__ + "  cargo:", self.cargo.x
	if (EV.STOP == 1):
	    print 'stop'
            newState =  "STATE2";
	else:
	    print 'no stop'
            newState =  "STATE3";

        sleep(DLY)
        return (newState, self.cargo)
    
    def state2(self, cargo):
	self.cargo.y *= 2
        print "STATE2 State in", self.__class__.__name__ + "  cargo:", self.cargo.x, self.cargo.y, self.cargo.name
        newState =  "STATE3";
        sleep(DLY)

	if (EV.RUN == 0):
	    print 'Not running'
	    EV.RUN = 1
	else:
	    print 'Running'

        return (newState, self.cargo)
    
    def state3(self, cargo):
	EV.STOP = 1
        print "STATE3 State in", self.__class__.__name__ + "  cargo:", self.cargo.x
        if (self.cargo.x == 5):
            newState =  "OUT_OF_RANGE";
        else:
            newState =  "STATE1";
    
	if (EV.SKIP == 1):
	    print 'skip'

        sleep(DLY)
        return (newState, self.cargo)

    def go(self):
	self.m.run(1)


if __name__ == "__main__":

    one = StateMachine_A()
    two = fsm6.StateMachine_B()

    EV = events.Events()

    print 40*'-'

    for i in range(0, 12):
        one.go()
        two.go()

