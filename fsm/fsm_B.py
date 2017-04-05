from time import sleep
import statemachine2 as sm
import events as ev
import inspect

DLY = 0.2

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
        print "%s %s: %s() - cargoB=%d %s" % (ev.bcolors.BLUE, \
	                            self.__class__.__name__, \
				    inspect.stack()[0][3], \
				    self.cargo.x, \
				    ev.bcolors.ENDC),
        newState =  "STATE2";

	if (self.EV.RUN == 1):
	    print "  %s %s %s" % (ev.bcolors.BLUE, 'RUN detected', ev.bcolors.ENDC)
            self.cargo.x += 1
	else:
	    print "  %s %s %s" % (ev.bcolors.BLUE, '---', ev.bcolors.ENDC)

        sleep(DLY)
        return (newState, self.cargo)
    
    def state2(self, cargo):
        print "%s %s: %s() - cargoB=%d %s" % (ev.bcolors.BLUE, \
	                            self.__class__.__name__, \
				    inspect.stack()[0][3], \
				    self.cargo.x, \
				    ev.bcolors.ENDC)
        newState =  "STATE3";

        sleep(DLY)
        return (newState, self.cargo)

    def state3(self, cargo):
        print "%s %s: %s() - cargoB=%d %s" % (ev.bcolors.BLUE, \
	                            self.__class__.__name__, \
				    inspect.stack()[0][3], \
				    self.cargo.x, \
				    ev.bcolors.ENDC)
	if (self.cargo.x == 2):
	    print "  %s %s %s" % (ev.bcolors.BLUE, 'enable STOP', ev.bcolors.ENDC)
	    self.EV.STOP = 1
	else:
	    print "  %s %s %s" % (ev.bcolors.BLUE, 'disable STOP', ev.bcolors.ENDC)
	    self.EV.STOP = 0

        newState =  "STATE1";

        sleep(DLY)
        return (newState, self.cargo)
    
    def go(self, ev):
        self.EV = ev
	self.m.run(1)
	return self.EV

