from time import sleep
import statemachine2 as sm
import events as ev

DLY = 0.4

class Cargo:
    name = ''
    x = 0
    y = 0

class StateMachine_B:
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
        self.m.add_state("STATE3", self.state3)
        self.m.add_state("OUT_OF_RANGE", None, end_state=1)
        self.m.set_start("STATE1")

    def state1(self, cargo):
        self.cargo.x += 1
        print "STATE1 State in", self.__class__.__name__ + "  cargo:", self.cargo.x
        newState =  "STATE2";

	if (self.EV.STOP == 1):
            print "STATE1 State in, EV_STOP", self.__class__.__name__
	    self.EV.SKIP = 0

        sleep(DLY)
        return (newState, self.cargo)
    
    def state2(self, cargo):
        print "STATE2 State in", self.__class__.__name__ + "  cargo:", self.cargo.x
        newState =  "STATE3";

	self.EV.SKIP = 1

        sleep(DLY)
        return (newState, self.cargo)

    def state3(self, cargo):
        print "STATE3 State in", self.__class__.__name__ + "  cargo:", self.cargo.x
        newState =  "STATE1";

        sleep(DLY)
        return (newState, self.cargo)
    
    def go(self, ev):
        self.EV = ev
	self.m.run(1)
	return self.EV

