var = 0

class bcolors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class FSM():
    def __init__(self, startState, cargo):
        print 'init'
	self.startState = startState
	self.running = 0
	self.nx = startState
	self.cargo = cargo

    def run(self):
        if (self.running == 0):
	    self.nx, self.cargo = self.startState(self.cargo)
	    self.running = 1
	    print 'cargo:', self.cargo

	else:
	    print '    running'
	    self.nx, self.cargo = self.nx(self.cargo)



# FSM1
def FSM1_state1(cargo):
    global var
    var += 1
    cargo = var
    print bcolors.GREEN + '  FSM1_state1' + bcolors.ENDC
    print '11 cargo', cargo
    nextState = FSM1_state2
    return nextState, cargo

def FSM1_state2(cargo):
    global var
    var += 1
    cargo = var
    print bcolors.GREEN + '  FSM1_state2' + bcolors.ENDC
    print '12 cargo', cargo
    nextState = FSM1_state3
    return nextState, cargo

def FSM1_state3(cargo):
    global var
    var += 1
    cargo = var
    print bcolors.GREEN + '  FSM1_state3' + bcolors.ENDC
    print '13 cargo', cargo
    nextState = FSM1_state1
    return nextState, cargo


# FSM2
def FSM2_state1(cargo):
    print bcolors.RED + '  FSM2_state1' + bcolors.ENDC
    nextState = FSM2_state2
    return nextState, cargo

def FSM2_state2(cargo):
    print bcolors.RED + '  FSM2_state2' + bcolors.ENDC
    nextState = FSM2_state3
    return nextState, cargo

def FSM2_state3(cargo):
    print bcolors.RED + '  FSM2_state3' + bcolors.ENDC
    nextState = FSM2_state1
    return nextState, cargo


fsm1 = FSM(FSM1_state1, 1)
fsm2 = FSM(FSM2_state1, 2)

for i in range(1, 8):
    fsm1.run()
    fsm2.run()

