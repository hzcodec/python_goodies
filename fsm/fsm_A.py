#   Auther      : Heinz Samuelsson
#   Date        : 2017-03-30
#   File        : fsm_A.py
#   Reference   : -
#   Description : Statemachine A.
#                 This can be used as a template for a statemachine.
#
#                 def __init__() - keep as the example below.
#
#                 def define_states() - define the states in the statemachine.
#                                       Shall contain 'OUT_OF_RANGE' and a set_start().
#      
#                 def go() - keep as the example below.
#
#   Python ver  : 2.7.3 (gcc 4.6.3)

from time import sleep
import statemachine2 as sm
import events as ev
import inspect

DLY = 0.1

# example of object holding information for this statemachine
class Cargo:
    name = ''
    x = 0
    y = 0


class StateMachine_A:
    def __init__(self):
	print 'Create', self.__class__.__name__
        self.m = sm.StateMachine()
	self.define_states()
	self.EV = ev.Events()

	# declare an object to hold data
	self.cargo = Cargo()

    def define_states(self):
        print 'Define states for', self.__class__.__name__
        self.m.add_state("STATE1", self.state1)
        self.m.add_state("STATE2", self.state2)
        self.m.add_state("OUT_OF_RANGE", None, end_state=1)
        self.m.set_start("STATE1")

    def state1(self, cargo):
        self.cargo.x += 1
        print "%s %s: %s() - cargoA=%d %s" % (ev.bcolors.GREEN, \
	                                      self.__class__.__name__, \
				              inspect.stack()[0][3], \
				              self.cargo.x, \
				              ev.bcolors.ENDC),

	if (self.cargo.x == 3):
	    print "  %s %s %s" % (ev.bcolors.GREEN, 'enable RUN', ev.bcolors.ENDC)
	    self.EV.RUN = 1
	else:
	    print "  %s %s %s" % (ev.bcolors.GREEN, '---', ev.bcolors.ENDC)

        newState = "STATE2";

        sleep(DLY)
        return (newState, self.cargo)
    
    def state2(self, cargo):
        print "%s %s: %s() - cargoA=%d %s" % (ev.bcolors.GREEN, \
	                                      self.__class__.__name__, \
				              inspect.stack()[0][3], \
				              self.cargo.x, \
				              ev.bcolors.ENDC),
        newState = "STATE1";

	if (self.EV.STOP == 1):
	    print "  %s %s %s" % (ev.bcolors.GREEN, 'STOP detected, disable RUN', ev.bcolors.ENDC)
	    self.cargo.x = 0
	    self.EV.RUN = 0
	else:
	    print "  %s %s %s" % (ev.bcolors.GREEN, '---', ev.bcolors.ENDC)

        sleep(DLY)
        return (newState, self.cargo)
    
    def go(self, ev):
        self.EV = ev
	self.m.run(1)
	return self.EV

