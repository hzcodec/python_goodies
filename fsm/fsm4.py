#   Auther      : Heinz Samuelsson
#   Date        : 2017-03-30
#   File        : fsm4.py
#   Reference   : http://gnosis.cx/publish/programming/charming_python_4.html
#   Description : FSM
#   Python ver  : 2.7.3 (gcc 4.6.3)

from time import sleep
from statemachine2 import *

DLY = 0.2

# statemachine m
def state1(val):
    val += 1
    print "STATE1 State:", val
    newState =  "STATE2";
    sleep(DLY)
    return (newState, val)

def state2(val):
    print  "STATE2 State:", val
    newState =  "STATE3";
    sleep(DLY)
    return (newState, val)

def state3(val):
    print  "STATE3 State:", val
    if (val == 3):
        newState =  "OUT_OF_RANGE";
    else:
        newState =  "STATE1";

    sleep(DLY)
    print val
    return (newState, val)


# statemachine n
def state11(val):
    val += 1
    print "STATE11 State:", val
    newState =  "STATE22";
    sleep(DLY)
    return (newState, val)

def state22(val):
    print  "STATE22 State:", val
    newState =  "STATE11";
    sleep(DLY)
    return (newState, val)


if __name__ == "__main__":

    m = StateMachine()
    n = StateMachine()

    m.add_state("STATE1", state1)
    m.add_state("STATE2", state2)
    m.add_state("STATE3", state3)
    m.add_state("OUT_OF_RANGE", None, end_state=1)

    n.add_state("STATE11", state11)
    n.add_state("STATE22", state22)

    m.set_start("STATE1")
    n.set_start("STATE11")

    for i in range(1, 12):
        m.run(0)
	n.run(0)
