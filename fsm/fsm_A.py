from time import sleep
import statemachine2 as sm
import events as ev

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
        print ev.bcolors.GREEN + "STATE1 State in", self.__class__.__name__ + "  cargo:", str(self.cargo.x) + ev.bcolors.ENDC

	if (self.EV.SKIP == 0):
	    print ev.bcolors.GREEN + 'no skip from A' + ev.bcolors.ENDC
	else:
	    print ev.bcolors.GREEN + 'skip from A and send STOP' + ev.bcolors.ENDC
	    self.EV.STOP = 1


        newState =  "STATE2";

        sleep(DLY)
        return (newState, self.cargo)
    
    def state2(self, cargo):
        print ev.bcolors.GREEN + "STATE2 State in", self.__class__.__name__ + "  cargo:", str(self.cargo.x) + ev.bcolors.ENDC
        newState =  "STATE1";

	if (self.EV.SKIP == 1):
	    self.EV.STOP = 0

        sleep(DLY)
        return (newState, self.cargo)
    
    def go(self, ev):
        self.EV = ev
	self.m.run(1)
	return self.EV

