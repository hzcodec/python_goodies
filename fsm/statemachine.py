#   Auther      : Heinz Samuelsson
#   Date        : 2017-03-30
#   File        : fsm3.py
#   Reference   : http://gnosis.cx/publish/programming/charming_python_4.html
#   Description : FSM
#   Python ver  : 2.7.3 (gcc 4.6.3)

from string import upper

class StateMachine:
    def __init__(self):
        self.handlers = {}
        self.startState = None
        self.endStates = []

    def add_state(self, name, handler, end_state=0):
        name = upper(name)
        self.handlers[name] = handler

        if end_state:
             self.endStates.append(name)

	     print self.handlers

    def set_start(self, name):
        self.startState = upper(name)

    def run(self, cargo):
        try:
            handler = self.handlers[self.startState]
        except:
            raise "InitializationError", "must call .set_start() before .run()"
        if not self.endStates:
            raise  "InitializationError", "at least one state must be an end_state"

        while 1:
            (newState, cargo) = handler(cargo)
            if upper(newState) in self.endStates:
                break
            else:
                handler = self.handlers[upper(newState)]


