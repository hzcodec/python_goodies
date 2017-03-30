from time import sleep
from statemachine import *

DLY = 0.2

# statemachine m
def state1(val):
    val += 1
    print "m : STATE1 State:", val
    newState =  "STATE2";
    sleep(DLY)
    return (newState, val)

def state2(val):
    print  "m : STATE2 State:", val
    newState =  "STATE3";
    sleep(DLY)
    return (newState, val)

def state3(val):
    print  "m : STATE3 State:", val
    if (val == 7):
        newState =  "Out_of_Range";
    else:
        newState =  "STATE1";

    sleep(DLY)
    return (newState, val)



if __name__ == "__main__":

    m = StateMachine()

    m.add_state("STATE1", state1)
    m.add_state("STATE2", state2)
    m.add_state("STATE3", state3)
    m.add_state("OUT_OF_RANGE", None, end_state=1)

    m.set_start("STATE1")

    m.run(0)
