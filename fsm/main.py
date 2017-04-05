import fsm_A
import fsm_B
import events

NO_OF_DELIMITERS = 50

def main():
    ev = events.Events()

    one = fsm_A.StateMachine_A()
    two = fsm_B.StateMachine_B()

    print NO_OF_DELIMITERS*'-'

    for i in range(0, 12):
        ev = one.go(ev)
	#print '----> SKIP:%d, RUN:%d, STOP:%d' % (ev.SKIP, ev.RUN, ev.STOP)
        #ev = two.go(ev)
	#print '----> SKIP:%d, RUN:%d, STOP:%d' % (ev.SKIP, ev.RUN, ev.STOP)

    print NO_OF_DELIMITERS*'-'


if __name__ == "__main__":
    main()

