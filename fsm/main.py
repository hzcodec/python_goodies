#!/usr/bin/env python

#   Auther      : Heinz Samuelsson
#   Date        : 2017-03-30
#   File        : main.py
#   Reference   : -
#   Description : Main program for fsm_A and FSM_B. The program is creating
#                 two instances of statemachines _A and _B.
#   Python ver  : 2.7.3 (gcc 4.6.3)

import fsm_A
import fsm_B
import events

NO_OF_DELIMITERS = 70

def main():
    event = events.Events()

    one = fsm_A.StateMachine_A()
    two = fsm_B.StateMachine_B()

    print NO_OF_DELIMITERS*'-'

    for i in range(0, 17):
        event = one.go(event)
        event = two.go(event)

    print NO_OF_DELIMITERS*'-'


if __name__ == "__main__":
    main()

