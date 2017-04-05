import fsm_A
import fsm_B
import events

NO_OF_DELIMITERS = 65

def main():
    event = events.Events()

    one = fsm_A.StateMachine_A()
    two = fsm_B.StateMachine_B()

    print NO_OF_DELIMITERS*'-'

    for i in range(0, 17):
        ev = one.go(event)
	#print '----> SKIP:%d, RUN:%d, STOP:%d' % (ev.SKIP, ev.RUN, ev.STOP)
        ev = two.go(event)
	#print '----> SKIP:%d, RUN:%d, STOP:%d' % (ev.SKIP, ev.RUN, ev.STOP)

    print NO_OF_DELIMITERS*'-'


if __name__ == "__main__":
    main()

