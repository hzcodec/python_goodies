#   Auther      : Heinz Samuelsson
#   Date        : 2017-03-30
#   File        : fsm5.py
#   Reference   : http://gnosis.cx/publish/programming/charming_python_4.html
#   Description : FSM
#   Python ver  : 2.7.3 (gcc 4.6.3)

from time import sleep
from statemachine2 import StateMachine

DLY = 0.2

class StateMachine_A:
    def __init__(self):
	print 'StateMachine A created'
        self.m = StateMachine()
	self.val = 0

    def define_states(self):
        print 'Define states for', self.__class__.__name__
        self.m.add_state("STATE1", self.state1)
        self.m.add_state("STATE2", self.state2)
        self.m.add_state("STATE3", self.state3)
        self.m.add_state("OUT_OF_RANGE", None, end_state=1)
        self.m.set_start("STATE1")

    def state1(self, val):
        self.val += 1
        print "STATE1 State in", self.__class__.__name__ + "  val:", self.val
        newState =  "STATE2";
        sleep(DLY)
        return (newState, self.val)
    
    def state2(self, val):
        print "STATE2 State in", self.__class__.__name__ + "  val:", self.val
        newState =  "STATE3";
        sleep(DLY)
        return (newState, self.val)
    
    def state3(self, val):
        print "STATE3 State in", self.__class__.__name__ + "  val:", self.val
        if (self.val == 5):
            newState =  "OUT_OF_RANGE";
        else:
            newState =  "STATE1";
    
        sleep(DLY)
        return (newState, self.val)

    def go(self):
        #print 'go'
	self.m.run(1)

class StateMachine_B:
    def __init__(self):
	print 'StateMachine B created'
        self.m = StateMachine()
	self.val = 0

    def define_states(self):
        print 'Define states for', self.__class__.__name__
        self.m.add_state("STATE1", self.state1)
        self.m.add_state("STATE2", self.state2)
        self.m.add_state("OUT_OF_RANGE", None, end_state=1)
        self.m.set_start("STATE1")

    def state1(self, val):
        self.val += 1
        print "STATE1 State in", self.__class__.__name__ + "  val:", self.val
        newState =  "STATE2";
        sleep(DLY)
        return (newState, self.val)
    
    def state2(self, val):
        print  "STATE2 State in", self.__class__.__name__ + "  val:", self.val
        newState =  "STATE1";

        if (self.val == 4):
            print  "Out of range! Quit application. Object:", self.__class__.__name__
            newState =  "OUT_OF_RANGE";
        else:
            newState =  "STATE1";
        sleep(DLY)
        return (newState, self.val)
    
    def go(self):
        #print 'go'
	self.m.run(1)


if __name__ == "__main__":

    one = StateMachine_A()
    two = StateMachine_B()
    print 40*'-'

    one.define_states()
    two.define_states()
    print 40*'-'

    for i in range(0, 12):
        one.go()
        two.go()

